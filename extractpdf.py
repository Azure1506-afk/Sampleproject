import os
import langchain
import pytesseract
from PyPDF2 import PdfReader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

#from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
def main():

    try:
        # Load the embedding model
        print("Loading embedding model...")
        embeddings = HuggingFaceEmbeddings()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()