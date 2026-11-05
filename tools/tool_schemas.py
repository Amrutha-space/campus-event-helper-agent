TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_open_events",
            "description": "Find open campus events on a given date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    }
                },
                "required": ["date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_event_details",
            "description": "Get complete details of a campus event.",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_id": {
                        "type": "string",
                        "description": "Unique event ID"
                    }
                },
                "required": ["event_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draft_registration_message",
            "description": "Draft a registration message for an event. Does not send it.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_name": {
                        "type": "string"
                    },
                    "event_id": {
                        "type": "string"
                    }
                },
                "required": ["student_name", "event_id"]
            }
        }
    }
]