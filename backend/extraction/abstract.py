# Function that extracts the asbtract section from raw PDFs
# The function suppports explicit abstract (using the 'Abstract' heading) 
# and implicit abstract (the first meaningful paragraph before the introduction)

import re #Regular expressions
from typing import Optional #Allows returning a string or None


# ---------- REGEX PATTERNS ----------#
#Compiled once for efficiency
#Match explicit headings (like 'abstract ' or 'A B S T R A C T')
ABSTRACT_HEADER_RE = re.compile(
    r"\bA\s*B\s*S\s*T\s*R\s*A\s*C\s*T\b|\bAbstract\b", 
    re.IGNORECASE,
)

#Match the first 'real' sentence
#Avoid titles, names, affilations
IMPLICIT_START_RE = re.compile(
    r"([A-Z][a-z]+(?:\s+[a-z]{2,}){3,}[^.!?]{40,}?\.)"
)

#Mark the end of an abstract
#Stops as it encounters these common words
STOP_RE = re.compile( 
    r"\bindex terms\b(\s*[—\-:]|\s)" #'index terms'
    r"|\bccs\s+concepts\b(\s*[•:—\-]|\s)" #'BCC concepts' - common in ACM papers
    r"|\badditional key words\b\s*:" #keywords
    r"|\bkeywords\b(\s*[:—-]|\s+[A-Z])"
    r"|1\s*\.?\s*introduction\b" #introduction
    r"|\bintroduction\b",
    re.IGNORECASE,
)

#Match comon footer noise (copyright information, download messages, journal page headers)
FOOTER_RE = re.compile(
    r"(†\s*Corresponding author.*$"
    r"|©\s*\d{4}.*$"
    r"|Downloaded from.*$" 
    r"|\d+\s+Data Intelligence.*$)",
    re.IGNORECASE,
) 


# ---------- HELPER FUNCTIONS ---------- #
#Clean extracted text (remove leading punctuation, whitespace, footer, normalize)
def _clean_abstract(text:str) -> str:
    text = text.strip(" :-\n") 
    text = re.sub(r"^[\s\.\-—]+", "", text)
    text = FOOTER_RE.sub("", text)
    return text.strip() 

#Truncate the text at firts occurence of a stop section (keywords, index terms, introduction)
def _cut_at_stop(text: str) -> str:
    match = STOP_RE.search(text)
    return text[:match.start()] if match else text 


# ---------- MAIN FUNCTION ----------#
#Extract explicit abstract ('abstract' or 'A B S T R A C T') or implicit abstract (first real paragraph before the introduction)
def extract_abstract(text: str) -> Optional[str]: 
    if not text:
        return None

    text = re.sub(r"\s+", " ",text) #Normalize whitespace

    #First attempt to extract explicit abstract
    explicit = ABSTRACT_HEADER_RE.search(text) 

    #Extract the text after 'abstract'
    if explicit:
        window = text[explicit.end(): explicit.end() + 6000]
        window = _cut_at_stop(window)
        abstract = _clean_abstract(window)

        if len(abstract) >=150: #Check if result is too short to plausibly be an abstract
            return abstract[:3000]
      

    #Extract implicit abstract (abstract section without a title)
    #Find the first real sentence (ensure no titles, names, institutions)
    sentence = IMPLICIT_START_RE.search(text)
    if not sentence:
        return None

    window = text[sentence.start(1): sentence.start(1) + 5000]
    window = _cut_at_stop(window)
    abstract = _clean_abstract(window)

    if len(abstract) < 200:
        return None
    
    return abstract[:3000]