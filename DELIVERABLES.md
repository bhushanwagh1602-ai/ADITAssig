# Assignment Deliverables

This document maps the requested outbound healthcare voice-agent deliverables to the submitted project files.

| Assignment deliverable | Submission evidence |
| --- | --- |
| Working implementation | `main.py` orchestrates the simulated outbound call, booking attempt, analysis, trace, and evaluation. Core logic is in `src/healthcare_voice_agent/`. |
| README with setup and usage | `README.md` provides local setup, demo, test, privacy, and architecture instructions. |
| Complete flow demonstration | Run `python main.py`. It prints the connected-call context, scheduling result, post-call summary, trace location, and evaluation. |
| Opik trace and evaluation | `OpikIntegration.log_call()` writes a JSON trace in `.opik_traces/`; `online_evaluation()` produces the `consultation_booking_outcome` result. The generated trace path is printed by the demo. |
| Standalone modular Opik integration | `src/healthcare_voice_agent/opik_integration.py` is independent of the call orchestration and can be replaced with an approved Opik SDK backend without changing the agent, booking, or analysis modules. |

## Demonstration procedure

```powershell
python main.py
```

Expected result: the console reports a `connected` call, a booked consultation with an `APT-...` confirmation ID, a post-call `booked` outcome, a local trace path, and a `pass` evaluation.

Open the emitted JSON trace:

```powershell
Get-Content .opik_traces\call-trace-1.json
```

The number will increase for each demo run. The trace contains call metadata, transcript, booking-tool output, audio reference, and post-call analysis. Direct identifiers in metadata are redacted by default.

## Validation evidence

```powershell
python -m pytest -q
```

The six automated tests cover successful booking, analysis, trace/evaluation, unavailable slots, input validation, and identifier redaction.

## Review notes

`LiveKitOutboundAgent` is deliberately a local, deterministic simulation because this repository does not contain LiveKit telephony credentials or a SIP/trunk configuration. The `OpikIntegration` component likewise writes a local-compatible trace without Opik credentials. Both adapter boundaries are intentionally isolated for production replacement. No real patient data should be used with the demo trace store.
