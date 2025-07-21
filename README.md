# Care Reply - AI Medical Bot 🩺

Care Reply is an intelligent, end-to-end chatbot designed to provide accurate answers to medical questions by leveraging a curated knowledge base. It utilizes a Retrieval-Augmented Generation (RAG) pipeline to ensure that responses are contextually relevant and grounded in the provided medical documents, preventing hallucinations and delivering trustworthy information.

## Features

-   **Ingest PDF Documents**: Easily load and process medical books or research papers in PDF format.
-   **Vector Knowledge Base**: Automatically creates a searchable vector database using Pinecone for efficient information retrieval.
-   **Accurate Responses**: Leverages Google's Gemini Pro and Generative AI Embeddings to understand questions and generate context-aware answers.
-   **User-Friendly Interface**: A simple web interface built with Flask allows for real-time interaction with the bot.

---

## Tech Stack & Architecture

-   **Large Language Model**: Google Gemini Pro
-   **Embeddings**: Google Generative AI Embeddings (`models/embedding-001`)
-   **Vector Database**: Pinecone
-   **Frameworks**: LangChain, Flask
-   **Data Processing**: PyPDF

The project follows a RAG architecture:
1.  **Data Ingestion**: Medical documents are loaded, split into manageable chunks, and converted into numerical embeddings.
2.  **Vector Storage**: These embeddings are stored in a Pinecone serverless index for fast similarity searches.
3.  **Retrieval & Generation**: When a user asks a question, it's embedded and used to retrieve relevant chunks from Pinecone. These chunks, along with the original question, are passed to the Gemini LLM to generate a final, context-grounded answer.

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/Aditya-Rai0/Care-Reply-AI-Medical-Bot.git
```
### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & Google credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
