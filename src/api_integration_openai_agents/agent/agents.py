# Base agent class or wrapper
from agents import Agent
from api_integration_openai_agents.agent import config

def spanish_agent():
    """Create a spanish translator agent instance."""
    agent: Agent = Agent(
        name="spanish_agent",
        instructions="You translate the user's message to spanish.",
        handoff_description="An English to Spanish translator.",
        model=config.gemini_model,
    )
    return agent

def french_agent():
    """Create a french translator agent instance."""
    agent: Agent = Agent(
        name="french_agent",
        instructions="You translate the user's message to french.",
        handoff_description="An English to french translator.",
        model=config.gemini_model,
    )
    return agent

def urdu_agent():
    """Create a urdu translator agent instance."""
    agent: Agent = Agent(
        name="urdu_agent",
        instructions="You translate the user's message to urdu.",
        handoff_description="An English to urdu translator.",
        model=config.gemini_model,
    )
    return agent

