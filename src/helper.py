
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_core.embeddings import Embeddings

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_google_genai import GoogleGenerativeAI






#Extract Data from the pdf File

def load_pdf_file(data):
    loader = DirectoryLoader(data,  glob = "*.pdf",
                  loader_cls = PyPDFLoader)
    documents = loader.load()
    return documents


# Split the Data into Text Chunks

def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks



 
