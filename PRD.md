# Product Requirements Document (PRD)

## 1. Overview
This project is a healthcare-focused outbound AI voice agent powered by LiveKit. The system will call a patient with their personal and clinical context, inform them about key health metrics, attempt to schedule a consultation, and then determine the final outcome after the conversation ends.

The solution must integrate with Opik for telemetry, trace capture, and evaluation of the completed call. The Opik integration should be modular and loosely coupled so it can be dropped into the LiveKit project with minimal changes.

## 2. Background and Context
The assignment brief requires a complete product flow:
- outbound call to a patient,
- use of patient identity and biomarkers,
- health metric explanation,
- scheduling simulation via a tool or function call,
- post-call outcome analysis,
- Opik tracking and evaluation.

The hidden project metadata available in the workspace does not include a .cloud folder; therefore this PRD is based on the assignment PDF, Task.md, and plan.md.

## 3. Product Goal
Create a working prototype that demonstrates a realistic healthcare outreach use case through an AI voice assistant, with transparent operational tracking and quality assessment.

## 4. Target Users
- Healthcare operations teams
- Care coordinators
- Clinical quality and monitoring teams
- Developers integrating LiveKit with observability tooling

## 5. Problem Statement
Healthcare outreach is often manual, repetitive, and hard to scale. A voice-first AI assistant can proactively contact patients, explain health metrics, and encourage follow-up action without requiring constant human supervision. The key challenge is to combine outbound voice interactions with relevant clinical data and accurate post-call analysis.

## 6. Goals
- Initiate a healthcare call with patient-specific context.
- Explain biomarker values such as glucose or HbA1c in a simple, actionable way.
- Attempt to schedule a doctor consultation.
- Record whether an appointment was booked.
- Analyze the conversation afterward and summarize the result.
- Send all relevant information to Opik for observability and evaluation.

## 7. Functional Requirements
### 7.1 Patient Data Input
The system must accept structured patient context including:
- Name
- Phone number
- Health biomarkers

### 7.2 Outbound Calling Flow
The system should:
- identify the patient to call,
- place the outbound call using LiveKit,
- greet the patient naturally,
- mention relevant health information,
- ask whether they would like to schedule a consultation.

### 7.3 Scheduling Simulation
The appointment flow may be simulated through a tool or function call, but it should behave like a real scheduling attempt.

The tool should:
- take relevant patient context,
- attempt booking the appointment,
- return a success or fail result,
- log the outcome for downstream analysis.

### 7.4 Post-Call Analysis
After the call ends, the system must:
- review the recorded transcript and call outcome,
- determine if the appointment was accepted,
- determine if the appointment was booked,
- summarize the final status in a clear output.

### 7.5 Opik Integration
The Opik module should be standalone and modular. It should capture:
- call metadata and variables,
- conversation transcript,
- recording or reference to the audio,
- tool call details and results,
- final post-call analysis.

### 7.6 Evaluation Requirement
At least one online evaluation in Opik must be implemented for the completed call.

Possible evaluation dimensions include:
- appointment booking success,
- conversation clarity,
- relevance of advice,
- professionalism and patient friendliness.

## 8. Non-Functional Requirements
- Scalability: the architecture should support reuse across multiple patient records.
- Observability: logs and traces should clearly show call flow and tool executions.
- Modularity: Opik integration should not be tightly coupled to the application core.
- Privacy: patient PII and medical data should be handled securely.
- Reliability: the system should mark call outcomes even when scheduling fails or the patient declines.

## 9. User Stories
### As a healthcare operations team member
I want to trigger an outbound voice call with patient context so that I can inform patients about important health information.

### As a care coordinator
I want the system to attempt a consultation booking so that patients can continue care without needing manual outreach.

### As a QA reviewer
I want post-call results to show whether an appointment was booked so that I can measure success and quality.

### As a developer
I want Opik tracing for each call so that I can inspect logs, transcripts, and tool results.

## 10. Success Criteria
The product is successful when:
- the outbound call can be initiated for a given patient profile,
- the AI agent communicates health metrics appropriately,
- a consultation attempt is made,
- the outcome is determined accurately after the call,
- Opik capture and evaluation are functioning,
- the architecture remains modular and reusable.

## 11. Acceptance Criteria
1. A patient profile with name, phone number, and clinical data can be passed into the agent.
2. A LiveKit-based outbound call is initiated.
3. The agent speaks about the patient’s health metrics in a natural, understandable way.
4. The agent attempts to schedule a consultation using a simulated tool call.
5. The call outcome is summarized after completion.
6. The metadata, transcript, and tool outputs are stored in Opik.
7. At least one online evaluation is created for the call.
8. The README documents how to run and validate the full flow.

## 12. Risks and Constraints
- Medical communication requires careful wording and privacy protection.
- Dialogue quality depends heavily on prompt and tool design.
- Real appointment booking may require an external backend outside the assignment scope.
- Opik trace logging must be implemented cleanly to avoid code entanglement.

## 13. Implementation Notes
The implementation path should follow the project plan:
1. Set up the LiveKit and app environment.
2. Build the healthcare outreach conversation.
3. Connect an appointment scheduling tool.
4. Add post-call analysis logic.
5. Integrate Opik as a standalone module.
6. Document the complete flow in a README.

## 14. Deliverables
- Working implementation
- README with setup and usage instructions
- End-to-end demonstration flow
- Opik trace and evaluation evidence
- Modular Opik integration component

## 15. Final Outcome
The final product will be a working prototype of an AI outbound healthcare voice agent that demonstrates the complete lifecycle from patient outreach to consultation scheduling and post-call evaluation using Opik.
