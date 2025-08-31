import dotenv

from dotenv import load_dotenv
import os   

load_dotenv()  # take environment variables from .env.test
API_KEY = os.getenv("OPENAI_API_KEY")
print(API_KEY)  

(print(f"API_KEY: {API_KEY}")   if API_KEY else print("API_KEY not found in environment variables"))
print("This is a test file for loading environment variables.")