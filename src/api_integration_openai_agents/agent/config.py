# OpenAI configuration (API keys, model settings, etc.)
import os
from dotenv import load_dotenv, find_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

def load_gemini_api_key() -> str | None:
    """Load environment variables from a .env file."""
    load_dotenv(find_dotenv())
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")
    # print("API_KEY: ", api_key)
    return api_key

GEMINI_API_KEY = load_gemini_api_key()
MODEL_NAME = "gemini-2.0-flash"

########################################################################################
gemini_provider = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

gemini_model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=gemini_provider,
)

gemini_runconfig = RunConfig(
    model=gemini_model,
    model_provider=gemini_provider,
    tracing_disabled=True,
)

def get_gemini_provider():
    """Load the OpenAI provider with the API key and base URL."""
    return gemini_provider

def get_gemini_model():
    """Load the OpenAI model with the API key and base URL."""
    return gemini_model

def get_gemini_runconfig():
    """Load the OpenAI run configuration with the API key and base URL."""
    return gemini_runconfig
