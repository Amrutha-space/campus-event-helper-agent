import json
from datetime import date

from tools.event_tools import (
    list_open_events,
    get_event_details,
    draft_registration_message
)

AVAILABLE_FUNCTIONS = {
    "list_open_events": list_open_events,
    "get_event_details": get_event_details,
    "draft_registration_message": draft_registration_message
}


def execute_tool(tool_call):

    function_name = tool_call.function.name

    try:
        arguments = json.loads(
            tool_call.function.arguments
        )

        if not isinstance(arguments, dict):
            return {"error": "Arguments must be a JSON object"}

        function = AVAILABLE_FUNCTIONS.get(function_name)

        if function is None:
            return {"error": "Tool is not allowed"}

        # Validate inputs
        if function_name == "list_open_events":
            date.fromisoformat(arguments["date"])

        elif function_name == "get_event_details":
            if not isinstance(arguments["event_id"], str):
                return {"error": "Invalid event ID"}

        elif function_name == "draft_registration_message":
            if not arguments["student_name"].strip():
                return {"error": "Student name cannot be empty"}

            if not isinstance(arguments["event_id"], str):
                return {"error": "Invalid event ID"}

        result = function(**arguments)

        return result

    except (ValueError, TypeError, KeyError) as error:
        return {"error": f"Invalid tool input: {error}"}

    except Exception:
        return {"error": "Tool execution failed"}