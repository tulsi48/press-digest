import streamlit as st
from rag_pipeline import ask_question

from ingest import process_urls

st.title("PressDigest 📰")

st.sidebar.header("Article URLs")
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]

if st.sidebar.button("Process"):
    valid_urls = [u for u in urls if u]
    if valid_urls:
        with st.spinner("Reading articles..."):
            process_urls(valid_urls)
        st.success("Ready for questions")

query = st.text_input("Ask something about the news")

if query:
    with st.spinner("Thinking..."):
        answer, sources = ask_question(query)

    st.header("Answer")
    st.write(answer)

    if sources:
        st.subheader("Sources")
        for s in sources.split("\n"):
            st.write(s)
