# import os
# from dotenv import load_dotenv
# load_dotenv()

# from src.helper import load_pdf_file, text_split

# from langchain_core.embeddings import Embeddings

# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# from pinecone.grpc import PineconeGRPC as Pinecone

# from pinecone import ServerlessSpec
# from langchain_pinecone import PineconeVectorStore



# GOOGLE_API_KEY=os.environ.get("GOOGLE_API_KEY")


# PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
# os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


# extracted_data=load_pdf_file(data='Data/')
# text_chunks=text_split(extracted_data)
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")



# pc = Pinecone(api_key=PINECONE_API_KEY)

# index_name = "medicalbot"


# pc.create_index(
#     name=index_name,
#     dimension=768, 
#     metric="cosine", 
#     spec=ServerlessSpec(
#         cloud="aws", 
#         region="us-east-1"
#     ) 
# ) 

# # Embed each chunk and upsert the embeddings into your Pinecone index.
# docsearch = PineconeVectorStore.from_documents(
#     documents=text_chunks,
#     index_name=index_name,
#     embedding=embeddings, 
# )

import os
from dotenv import load_dotenv

# 1. Load environment variables from your .env file
load_dotenv()

# --- IMPORTS ---
from src.helper import load_pdf_file, text_split
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# 2. Get API keys and validate them
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

if not GOOGLE_API_KEY or not PINECONE_API_KEY:
    raise ValueError("Google and/or Pinecone API keys not found. Please check your .env file.")

# 3. Load data and initialize embeddings
print("Loading data and initializing embeddings...")
extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
print("Data loaded and embeddings initialized.")

# 4. Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"

# 5. Check if the index already exists before creating
print(f"Checking for index '{index_name}'...")
if index_name not in pc.list_indexes().names():
    print(f"Index '{index_name}' not found. Creating a new one...")
    pc.create_index(
        name=index_name,
        dimension=768, 
        metric="cosine", 
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print("Index created successfully.")
else:
    print(f"Index '{index_name}' already exists.")

# 6. Upsert documents into the index
print("Upserting documents into Pinecone index...")
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)
print("Documents have been successfully upserted.")