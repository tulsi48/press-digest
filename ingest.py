from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings
from utils import save_vectorstore

def process_urls(urls):

    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = splitter.split_documents(data)

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    save_vectorstore(vectorstore)
