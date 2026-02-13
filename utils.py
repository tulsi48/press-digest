import pickle
import os
from config import VECTOR_PATH

def save_vectorstore(vs):
    os.makedirs("faiss_index", exist_ok=True)
    with open(VECTOR_PATH, "wb") as f:
        pickle.dump(vs, f)

def load_vectorstore():
    if not os.path.exists(VECTOR_PATH):
        return None
    with open(VECTOR_PATH, "rb") as f:
        return pickle.load(f)
