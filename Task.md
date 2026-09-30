# Task: Outbound AI Voice Agent for Healthcare

## Objective
Build an outbound AI voice agent using LiveKit for a healthcare scenario. The agent should call a person using provided contextual information such as:

- Name
- Phone number
- Relevant health biomarkers (for example blood glucose or HbA1c)

During the call, the agent must inform the person about their health metrics and attempt to schedule a doctor consultation. The scheduling portion may be simulated using a tool or function call.

## Required functionality
### 1. Outbound call flow
- Use LiveKit to place an outbound call to a person.
- Populate the call with patient information and health metric context.
- Have the voice agent explain the person's health status using the supplied biomarkers.
- Attempt to book a medical consultation.

### 2. Post-call analysis
- After the call ends, analyze the conversation and determine the outcome.
- Record whether an appointment was successfully booked or not.
- Summarize the result in an actionable way for review.

### 3. Opik integration
Integrate Opik and send the relevant call information, including:

- Call metadata and variables
- Conversation/transcript
- Call recording or audio reference
- Tool calls and results
- Post-call analysis

Also implement at least one online evaluation in Opik for the completed call. The evaluation approach is flexible but should be meaningful.

The Opik integration should be modular and standalone, ideally as a single file or module, so it can be dropped into the LiveKit project with minimal changes to the core app.

## Deliverables
- Working implementation
- README with setup and usage instructions
- Demonstration of the complete flow from outbound call to post-call analysis and Opik
- Opik trace/evaluation for the call
- Modular Opik integration

## Review expectations
The implementation will be reviewed in detail, and the developer should be prepared to explain the code, architecture, and technical decisions behind the solution.
