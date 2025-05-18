# Base agent class or wrapper
from agents import Agent
from api_integration_openai_agents.agent import config
from api_integration_openai_agents.agent.tools import get_application_owner_details

def create_base_agent():
    """Create a base agent instance."""

    agent: Agent = Agent(
        name="MyAssistant",
        instructions="You are a helpful assistant. user `getApplicationOwnerDetails` to get the application owner details.",
        tools=[get_application_owner_details],
        model=config.gemini_model,
    )

    return agent
