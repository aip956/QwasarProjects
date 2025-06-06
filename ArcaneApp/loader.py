from pathlib import Path
import re

def load_documents(folder_path="documents"):
    """
    Load all text files from the specified folder and return their content as a list of strings.
    
    Args:
        folder_path (str): The path to the folder containing text files.
        
    Returns:
        list: A list of strings, each representing the content of a text file.
    """
    documents = []
    for file_path in Path(folder_path).glob("*.txt"):
        print(f"Loading file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            chunks = chunk_text(text)
            documents.extend(chunks)
    
    return documents

def chunk_text(text, chunk_size=500):
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# the load_documents will 
# Look inside the documents folder
# Read all text files
# Normalize whitespace
# Split text into chunks of 500 characters (chunk_text)
# Return a list of text chunks
# This function is used in rag_engine.py to load documents for building the vector store.
# It is also used in main.py to load documents when the app starts.
# This allows the app to answer questions based on the content of the documents.