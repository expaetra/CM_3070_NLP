#Function that converts a PDF file into pain text for furhter processing

from pathlib import Path #Ensure safe and Os independent file paths
from pypdf import PdfReader #Library for extracting text from PDFs
import re #Regular expressions
import logging #Debugging

logger = logging.getLogger(__name__) #Create logger

#Extract and normalize text
def extract_text_from_pdf(path: Path) ->str: 
    logger.info(f"Extracting text from {path.name}") #Log which file is being processed

    reader = PdfReader(path) #Open the file using PyPDF
    
    #Aggregate the text from all files
    text = ""
    for page in reader.pages: #Extract text from each page
        text += page.extract_text() or "" 

    logger.info(f"Extracted {len(text)}characters") #Debugging
    return re.sub(r"\s+", " ", text) #Normalize whitespaces
