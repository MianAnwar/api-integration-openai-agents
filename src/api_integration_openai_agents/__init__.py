import asyncio
from agents import Agent, Runner, set_default_openai_api, set_default_openai_client, set_tracing_disabled
from api_integration_openai_agents.agent import config
from api_integration_openai_agents.agent.base_agent import create_base_agent
from api_integration_openai_agents.agent.agents import spanish_agent, french_agent, urdu_agent

print("Environment variables loaded successfully.")
print("GEMINI_API_KEY: ", config.GEMINI_API_KEY)
print("MODEL_NAME: ", config.MODEL_NAME)

set_default_openai_client(client=config.get_gemini_provider(), use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)

async def run_agent():
    """Run the agent with a sample input."""    
    base_agent: Agent = create_base_agent()
    
    base_agent.tools.append(spanish_agent().as_tool(
        tool_name="translate_to_spanish",
        tool_description="Translate the user's message to Spanish.",
    ))
    base_agent.tools.append(french_agent().as_tool(
        tool_name="translate_to_french",
        tool_description="Translate the user's message to French.",
    ))
    base_agent.tools.append(urdu_agent().as_tool(
        tool_name="translate_to_urdu",
        tool_description="Translate the user's message to Urud.",
    ))
    
    input_text = "What is the application owner details? Translate to Urdu."
    result = await Runner.run(base_agent, input=input_text, run_config=config.gemini_runconfig)
    print("Result: ", result.final_output)

# This is a placeholder for the main function of the package.
def main() -> None:
    asyncio.run(run_agent())
    print("Hello from api-integration-openai-agents!")
