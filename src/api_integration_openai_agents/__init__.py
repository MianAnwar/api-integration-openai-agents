import asyncio
from agents import Agent, Runner
from api_integration_openai_agents.agent import config
from api_integration_openai_agents.agent.base_agent import create_base_agent

print("Environment variables loaded successfully.")
print("GEMINI_API_KEY: ", config.GEMINI_API_KEY)
print("MODEL_NAME: ", config.MODEL_NAME)

async def run_agent():
    """Run the agent with a sample input."""
    base_agent: Agent = create_base_agent()
    input_text = "What is the application owner details?"
    result = await Runner.run(base_agent, input=input_text, run_config=config.gemini_runconfig)
    print("Result: ", result.final_output)

# This is a placeholder for the main function of the package.
def main() -> None:
    asyncio.run(run_agent())
    print("Hello from api-integration-openai-agents!")
