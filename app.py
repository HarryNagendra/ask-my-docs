import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import requests

st.write("Upload PDFs and ask questions from your documents using AI.")

st.title("📄 Ask My Docs")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)

question = st.text_input("Ask a question")

def split_text(text, chunk_size=1000):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks

if uploaded_files:

    all_chunks = []

    for file in uploaded_files:

        pdf_reader = PdfReader(file)

        text = ""

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        chunks = split_text(text)

        all_chunks.extend(chunks)

    st.write("Total Chunks:", len(all_chunks))

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(all_chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    st.success("Embeddings created successfully!")

    if question:

        question_embedding = model.encode([question])

        distances, indices = index.search(
            np.array(question_embedding),
            k=3
        )

        relevant_chunks = []

        st.subheader("Source Chunks")

        for i in indices[0]:

            relevant_chunks.append(all_chunks[i])

            st.write(all_chunks[i])
            st.write("------")

        context = "\n".join(relevant_chunks)

        prompt = f"""
Answer only from the context below.

If answer is not present, say:
"I don't know based on these documents."

Context:
{context}

Question:
{question}
"""

        st.subheader("Answer")

        API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

        headers = {
            "Authorization": "Bearer YOUR_API_KEY"
        }

        payload = {
            "inputs": prompt
        }

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload
        )

        result = response.json()

        st.write(result[0]["generated_text"])
