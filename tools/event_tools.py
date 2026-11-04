# tools/event_tools.py

# Sample campus event database
EVENTS = [
    {
        "event_id": "EVT001",
        "name": "AI Project Clinic",
        "date": "2026-11-10",
        "time": "10:00 AM - 1:00 PM",
        "venue": "Computer Science Block",
        "description": "Build and discuss practical AI projects.",
        "eligibility": "All college students",
        "fee": 0,
        "deadline": "2026-11-08",
        "registration_open": True
    },
    {
        "event_id": "EVT002",
        "name": "Web Development Sprint",
        "date": "2026-11-10",
        "time": "2:00 PM - 5:00 PM",
        "venue": "Innovation Lab",
        "description": "A hands-on frontend and backend coding sprint.",
        "eligibility": "B.Tech students",
        "fee": 100,
        "deadline": "2026-11-09",
        "registration_open": True
    },
    {
        "event_id": "EVT003",
        "name": "Campus Hackathon",
        "date": "2026-11-15",
        "time": "9:00 AM - 6:00 PM",
        "venue": "Main Auditorium",
        "description": "A team-based 24-hour innovation challenge.",
        "eligibility": "All college students",
        "fee": 0,
        "deadline": "2026-11-12",
        "registration_open": False
    }
]


# TOOL 1: List open events
def list_open_events(date: str):
    """
    Find events scheduled on a given date
    that are currently accepting registrations.
    """

    matching_events = []

    for event in EVENTS:
        if (
            event["date"] == date
            and event["registration_open"]
        ):
            matching_events.append({
                "event_id": event["event_id"],
                "name": event["name"],
                "date": event["date"],
                "time": event["time"],
                "venue": event["venue"]
            })

    return {"events": matching_events}


# TOOL 2: Get event details
def get_event_details(event_id: str):
    """
    Retrieve complete details about a particular event.
    """

    for event in EVENTS:
        if event["event_id"] == event_id:
            return event

    return {"error": "Event not found"}


# TOOL 3: Draft registration message
def draft_registration_message(
    student_name: str,
    event_id: str
):
    """
    Generate a registration message for the student.
    """

    event = get_event_details(event_id)

    if "error" in event:
        return event

    if not event["registration_open"]:
        return {"error": "Registration is currently closed"}

    message = f"""
Subject: Registration Request - {event['name']}

Hello Event Coordinator,

My name is {student_name}.

I am interested in registering for
{event['name']} scheduled on {event['date']}.

Please let me know the registration procedure
and any additional requirements.

Thank you.

Regards,
{student_name}
"""

    return {"draft_message": message}