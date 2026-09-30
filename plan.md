# Assignment plan

## Problem
Build an outbound AI voice agent in a LiveKit healthcare scenario that calls a patient with name, phone, and biomarker data; informs them about their health metrics; attempts to schedule a doctor consultation; analyzes the outcome after the call; and sends the relevant details to Opik with an online evaluation.

## Proposed approach
1. Set up the project scaffold and required dependencies for a LiveKit-based voice agent and Opik integration.
2. Implement the outbound call flow using a healthcare patient profile and a simulated appointment booking tool.
3. Capture transcripts, call metadata, tool results, and audio references, then perform a post-call outcome analysis.
4. Add a modular Opik integration that logs traces and at least one evaluation for the completed call.
5. Document setup and usage in a README and verify the complete flow from call to analysis.

## Todo list
- Review assignment requirements
- Set up project scaffold
- Build outbound voice agent
- Add post-call analysis
- Integrate Opik tracing and evaluation
- Prepare README and demo deliverables

## Notes
- The assignment explicitly requires a healthcare use case and outbound calling behavior driven by patient metadata.
- Appointment booking may be simulated via a tool/function call but should still reflect a realistic scheduling workflow.
- Opik integration must be modular and plugin-friendly with minimal changes to the core LiveKit app.
- Deliverables include a working implementation, README, demonstration flow, and Opik trace/evaluation evidence.
