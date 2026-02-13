from langchain_openai import ChatOpenAI
from config import OPENROUTER_API_KEY, MODEL_NAME

def get_llm():
    return ChatOpenAI(
        model=MODEL_NAME,
        temperature=0.7,
        max_tokens=500,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
    )
