from tools.event_tools import (
    list_open_events,
    get_event_details,
    draft_registration_message
)

# Test 1: Find events on November 10
print(list_open_events("2026-11-10"))

# Test 2: Find an event that is closed
print(get_event_details("EVT003"))

# Test 3: Try an invalid event ID
print(get_event_details("EVT999"))

# Test 4: Draft a registration message
print(
    draft_registration_message(
        "Amrutha",
        "EVT002"
    )
)
