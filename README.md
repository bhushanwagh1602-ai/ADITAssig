# Outbound Healthcare Voice Agent

This project is a working prototype for an outbound AI voice agent built for a healthcare use case. It demonstrates:

- an outbound call flow using patient context,
- biomarker-based health messaging,
- appointment booking simulation,
- post-call analysis,
- modular Opik trace logging and evaluation.

## Project goals

The system follows the assignment brief from the PDF and the project PRD:

1. Call a patient using known data such as name, phone number, and biomarkers.
2. Inform them about blood glucose and HbA1c values.
3. Attempt to schedule a doctor consultation.
4. Analyze whether the consultation was booked.
5. Send the call and evaluation data to Opik.

## Architecture

The project is intentionally simple and modular:

- `main.py` — demo entry point
- `src/healthcare_voice_agent/models.py` — patient and call data models
- `src/healthcare_voice_agent/livekit_agent.py` — outbound call orchestration
- `src/healthcare_voice_agent/appointment_tool.py` — scheduling simulation
- `src/healthcare_voice_agent/post_call_analysis.py` — outcome analysis
- `src/healthcare_voice_agent/opik_integration.py` — modular Opik adapter

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install pytest
```

### 3. Run the demo

```bash
python main.py
```

This runs a sample healthcare call flow using a demo patient profile.

### 4. Run tests

```bash
python -m pytest -q
```

For the assignment submission checklist and a reproducible demonstration procedure, see [DELIVERABLES.md](DELIVERABLES.md).

## Demo flow

The demo does the following:

1. Creates a patient profile with a name, phone number, glucose value, and HbA1c value.
2. Starts a simulated outbound call.
3. Builds a short conversation script explaining the health metrics.
4. Simulates patient acceptance and schedules a consultation.
5. Analyzes the final call outcome.
6. Writes a trace file in the `.opik_traces` directory.
7. Produces an Opik-style evaluation summary.

## Opik integration

The project includes a modular Opik adapter in `src/healthcare_voice_agent/opik_integration.py`.

It logs:
- patient metadata,
- transcript snippets,
- tool call output,
- post-call analysis,
- an evaluation score.

The implementation is designed to work in a local/offline environment without requiring a live Opik backend. It writes JSON traces using a pseudonymous patient ID and redacts direct identifiers by default. Pass `include_pii=True` only when the trace store is approved for protected health information.

The trace includes the booking attempt and result, transcript, audio reference, post-call analysis, and the `consultation_booking_outcome` evaluation. For production, replace the local adapter's storage call with the approved Opik SDK/client and use the organization’s access controls and retention policy.

## Outcome handling

The booking simulator records three distinct outcomes: booked, declined, and accepted-but-slot-unavailable. Post-call analysis returns a clear `outcome` and `next_action`, so operations can distinguish a refusal from a scheduling-system failure.

## Notes on LiveKit

This prototype intentionally avoids hard dependencies on a real telephony stack so it can run in a local development environment. The `LiveKitOutboundAgent` is structured to be extended with a real LiveKit client when credentials and runtime infrastructure are available.

## Suggested next steps

- connect to a real LiveKit room / token flow,
- replace the booking simulator with a real scheduling backend,
- add actual Opik SDK calls and environment configuration,
- expand the conversation flow with a real voice model and turn-taking pipeline.
