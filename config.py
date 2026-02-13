import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "mistralai/mistral-7b-instruct"

VECTOR_PATH = "faiss_index/store.pkl"
