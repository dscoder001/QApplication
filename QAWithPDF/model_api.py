import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from custom_logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        model = Gemini(api_key=api_key, models='gemini-1.5-flash')
        return model
    except Exception as e:
        raise customexception(e, sys)
