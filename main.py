from __future__ import annotations

from src.healthcare_voice_agent import (
    AppointmentBookingTool,
    LiveKitOutboundAgent,
    OpikIntegration,
    PatientProfile,
    analyze_call_outcome,
)


def build_demo_patient() -> PatientProfile:
    return PatientProfile(
        name="Aditi Sharma",
        phone_number="+1-415-555-0189",
        blood_glucose=168.0,
        hba1c=8.6,
        preferred_slot="Tomorrow at 10:00 AM",
        doctor_type="primary care",
    )


def run_demo() -> dict:
    patient = build_demo_patient()

    livekit_agent = LiveKitOutboundAgent(patient)
    call_context = livekit_agent.place_call()
    transcript = livekit_agent.build_conversation()
    patient_response = livekit_agent.evaluate_response(patient_agreed=True)

    booking_tool = AppointmentBookingTool()
    appointment_result = booking_tool.schedule(patient, patient_agreed=(patient_response == "accepted"))
    analysis = analyze_call_outcome(transcript, appointment_result)

    opik = OpikIntegration()
    trace_record = opik.log_call(
        patient=patient,
        transcript=transcript,
        tool_result=appointment_result,
        analysis=analysis,
        audio_reference="demo-recording://outbound-call-001",
    )
    evaluation = opik.online_evaluation(analysis)

    return {
        "call_context": call_context,
        "transcript": transcript,
        "appointment_result": {
            "appointment_booked": appointment_result.appointment_booked,
            "scheduled_time": appointment_result.scheduled_time,
            "confirmation_id": appointment_result.confirmation_id,
            "status_message": appointment_result.status_message,
        },
        "analysis": analysis,
        "trace_record": trace_record,
        "evaluation": evaluation,
    }


if __name__ == "__main__":
    result = run_demo()
    print("Outbound healthcare call demo completed.")
    print(result["call_context"])
    print(result["analysis"]["summary"])
    print(result["trace_record"])
    print(result["evaluation"])
