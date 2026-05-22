# Ask My Docs

## Candidate Details

- Name: Nagendra B V
- Email: driftynagendra@gmail.com
- Phone: 8105492517
- Role Applied: AI Developer Internship

---

## Project Overview

Ask My Docs is a RAG (Retrieval-Augmented Generation) based PDF Question Answering application built using Streamlit, Sentence Transformers, and FAISS.

Users can upload PDF documents, ask questions in natural language, and receive answers based on the content of the uploaded PDFs along with relevant source chunks.

---

## Features

- Upload multiple PDF files
- Extract text from PDFs
- Split text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings using FAISS vector database
- Retrieve relevant chunks based on user query
- Display source chunks
- Streamlit-based web interface
- LLM integration using Hugging Face Inference API

---

## Technologies Used

- Python
- Streamlit
- Sentence Transformers
- FAISS
- PyPDF2
- NumPy
- Requests
- Hugging Face Inference API

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK

---

##Move into project folder

```bash
cd ask-my-docs

---

##Run application 

```bash
python -m streamlit run app.py

---

##API Setup
Create a .env file or directly add your API key in the code

Example:

HUGGINGFACE_API_KEY=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

---

## requirements.txt

streamlit
PyPDF2
sentence-transformers
faiss-cpu
numpy
requests
torch
torchvision

---

## Project Architecture
1. Upload PDFs
2. Extract PDF text
3. Split text into chunks
4. Generate embeddings using Sentence Transformers
5. Store vectors in FAISS
6. Retrive relevant chunks for user question
7. Send retrieved context to LLM
8. Display generated answer and source chunks

---

## Sample Questions and Answers
Q1

Question:
What is the objective of the project?

Answer:
The objective of the project is to build a RAG-based PDF Question Answering system.

Q2

Question:
Which vector database is used?

Answer:
FAISS vector database is used to store embeddings.

Q3

Question:
Which embedding model is used?

Answer:
The application uses the all-MiniLM-L6-v2 Sentence Transformer model.

Q4

Question:
Which framework is used for UI?

Answer:
Streamlit is used for the web interface.

Q5

Question:
What happens if answer is not available?

Answer:
The application responds that it does not know based on the provided documents.

##Features Status

**Completed Features

PDF Upload
PDF Text Extraction
Text Chunking
Embeddings Generation
FAISS Vector Storage
Retrieval Pipeline
Streamlit UI
Source Chunk Display

**Partially Completed
LLM API integration

**Not Implemented
Multi-turn memory
Page number citations

**Known Limitations
API responses may fail during internet connectivity issues
Large PDFs may increase processing time
Some answers may depend on external API availability

**Future Improvements
Add conversation memory
Add page number citations
Improve UI design
Add embedding caching
Improve chunk ranking

##Demo Recording
Video Link

##Live Deployment
Streamlit deployment link here

Repository Link
GitHub respository link
