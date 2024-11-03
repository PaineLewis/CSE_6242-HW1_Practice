###py file to connect to TMDb API
import os
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY')

