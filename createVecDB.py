import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

def create_vector_db(pdf_directory: str, db_directory: str):
    """
    Reads PDFs from a directory, processes them, and stores them in ChromaDB.
    """
    # 2. Load all PDFs from the specified directory
    print(f"Loading PDFs from '{pdf_directory}'...")
    loader = PyPDFDirectoryLoader(pdf_directory)
    documents = loader.load()
    print(f"Successfully loaded {len(documents)} PDF pages.")

    # 3. Split the text into optimal chunks for embedding
    print("Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       # Number of characters per chunk
        chunk_overlap=200,     # Overlap to maintain context between chunks
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    # 4. Initialize the embedding model
    embeddings = HuggingFaceEmbeddings(model="text-embedding-3-small")

    # 5. Create and persist the vector database
    print(f"Creating vector database at '{db_directory}'...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=db_directory
    )
    
    print("✅ Vector database successfully created and saved!")
    return vector_db

if __name__ == "__main__":
    # Define your folders
    PDF_INPUT_FOLDER = "./my_pdfs"   # Create this folder and drop your PDFs inside
    DB_OUTPUT_FOLDER = "./chroma_db"  # The database will be saved here
    
    # Ensure input folder exists for the demo
    os.makedirs(PDF_INPUT_FOLDER, exist_ok=True)
    
    # Run the builder
    # Note: Ensure you have placed PDFs in './my_pdfs' before running
    db = create_vector_db(PDF_INPUT_FOLDER, DB_OUTPUT_FOLDER)