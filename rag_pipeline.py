from langchain_classic.chains import RetrievalQAWithSourcesChain
from llm_provider import get_llm
from utils import load_vectorstore

def ask_question(query):

    vectorstore = load_vectorstore()
    if vectorstore is None:
        return "No data processed yet.", ""

    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=get_llm(),
        retriever=vectorstore.as_retriever()
    )

    result = chain({"question": query}, return_only_outputs=True)
    return result["answer"], result.get("sources", "")
