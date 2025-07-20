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

---

## Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Aditya-Rai0/CareReply---AI-Patient-Message-Responder.git

2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

Bash

python -m venv .venv
Activate the environment:

Windows:

Bash

.\.venv\Scripts\activate
macOS / Linux:

Bash

source .venv/bin/activate
3. Install Dependencies
Install all the required Python packages.

Bash

pip install -r requirements.txt
(Note: If you don't have a requirements.txt file, you can create one with pip freeze > requirements.txt after installing all necessary packages.)

4. Set Up Environment Variables
Create a file named .env in the root directory of the project and add your API keys:

GOOGLE_API_KEY="your_google_api_key_here"
PINECONE_API_KEY="your_pinecone_api_key_here"

How to Run the Project
The project has two main parts: indexing the data and running the web application.

Step 1: Create the Knowledge Base
First, you need to process your documents and store them in the Pinecone index. Place your PDF files inside the Data/ directory.

Then, run the store_index.py script. You only need to do this once.

Bash

python store_index.py
This will load the PDFs, create embeddings, and upload them to your "medicalbot" index in Pinecone.

Step 2: Run the Web Application
Once the index is populated, start the Flask web server.

Bash

python app.py
Open your web browser and navigate to http://127.0.0.1:8080 to start chatting with your medical bot.