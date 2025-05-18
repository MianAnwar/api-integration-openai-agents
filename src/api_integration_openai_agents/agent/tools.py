# Tool definitions used by agents
from agents import function_tool

@function_tool("get_current_weather")
def get_current_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    """
    # This is a placeholder implementation. In a real implementation, you would
    # use an API to get the current weather for the given location.
    return f"The current weather in {location} is sunny."

@function_tool("getApplicationOwnerDetails")
def get_application_owner_details() -> str:
    """
    Fetch Application Owner Details.
    """
    return {"name": "John Doe", "email": ""}
