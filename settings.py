from dotenv import load_dotenv
import os

load_dotenv()

def get_token():
    TOKEN = os.getenv('TOKEN')
    if TOKEN is None:
        raise ValueError('TOKEN yoq')
        
    return TOKEN

def get_api_key():
    API_KEY = os.getenv('API_KEY')
    if API_KEY is None:
        raise ValueError('API_KEY yoq')
        
    return API_KEY
    
