# PressDigest 📰

AI-powered News Research & Summarization using RAG (Retrieval Augmented Generation)

---

## Overview

PressDigest lets users paste news article URLs and ask questions about them.
The system reads articles, builds a searchable knowledge base, and generates answers with sources.

Instead of a simple summarizer, this project performs **context-aware reasoning across multiple articles** using a local vector database and an LLM.

---

## Features

* Multi-article ingestion from URLs
* Semantic search over article content
* Source-backed answers
* Free local embeddings (no paid embedding API)
* OpenRouter LLM integration
* Persistent FAISS vector storage
* Streamlit interactive UI

---

## Tech Stack

* **LLM:** OpenRouter (Mistral / Llama / Gemma supported)
* **Embeddings:** sentence-transformers (local)
* **Vector DB:** FAISS
* **Framework:** LangChain (modular)
* **Frontend:** Streamlit
* **Language:** Python

---

## Project Structure

```
newsbrief/
│
├── app.py                # Streamlit UI
├── config.py             # Environment + constants
├── llm_provider.py       # LLM connection (OpenRouter)
├── embeddings.py         # Local embedding model
├── ingest.py             # Article loading + chunking
├── rag_pipeline.py       # Question answering logic
├── utils.py              # Save/load vector DB
└── faiss_index/          # Stored vectors
```

---

## Installation

### 1) Clone

```
git clone <repo-url>
cd newsbrief
```

### 2) Create environment

```
python -m venv venv
venv\Scripts\activate      (Windows)
source venv/bin/activate   (Linux/Mac)
```

### 3) Install dependencies

```
pip install streamlit
pip install langchain langchain-community langchain-openai langchain-classic
pip install langchain-text-splitters
pip install sentence-transformers faiss-cpu unstructured python-dotenv
```

---

## API Key Setup

Create a `.env` file:

```
OPENROUTER_API_KEY=your_key_here
```

Get key from: https://openrouter.ai

---

## Run the App

```
streamlit run app.py
```

---

## How It Works

1. User enters article URLs
2. Articles are scraped and split into chunks
3. Local embeddings convert text → vectors
4. FAISS stores vectors for semantic retrieval
5. User asks a question
6. Relevant context retrieved
7. LLM generates answer with sources

---

## Example Use Cases

* Research news quickly
* Compare multiple reports
* Verify claims across articles
* Extract facts without reading full articles

---

## Future Improvements

* Chat history memory
* Highlighted source sentences
* Auto daily news ingestion
* Multi-topic knowledge base
* Streaming responses

---

## License

MIT
