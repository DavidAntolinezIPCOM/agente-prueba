from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import MAIN_PROMPT

model = LiteLlm(
    model="openai/gpt-5.1"  #modelo(empresa)/version - anthropic/claude-3.0, openai/gpt-5.1, 
)

root_agent = Agent(
    model=model,
    name='root_agent',
    description='Eres Clara, la asistente virtual de la Compañía Hotelera. Tu tarea es ayudar a los huéspedes a crear nuevas reservas, gestionar sus reservas existentes y resolver consultas generales sobre los servicios del hotel.',
    instruction=MAIN_PROMPT,
)
