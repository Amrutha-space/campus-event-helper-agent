# Agent Tools Plan

## Project: Campus Event Helper

### User Goal
Help students discover upcoming college events,
check event details, and prepare registration messages.

### Tools the Agent May Call

#### 1. list_open_events
- Purpose: Find events available on a particular date.
- Inputs: date
- Output: Event names, timings, venue.

#### 2. get_event_details
- Purpose: Retrieve complete information about an event.
- Inputs: event_id
- Output: Description, eligibility, fee, registration deadline.

#### 3. draft_registration_message
- Purpose: Generate a registration message.
- Inputs: student_name, event_id
- Output: Registration message.

### Tools the Agent Must NOT Call Yet

- send_message
- make_payment
- update_database

### Safety Rules
- The agent can read event information.
- The agent can draft messages.
- The agent cannot send messages without approval.
- The agent cannot make payments.
- The agent cannot modify event records.

### Initial Scope
This version is read-only, except for generating
draft messages. All external actions require
future implementation and user approval.