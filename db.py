import os
from supabase import create_client, Client
from dotenv import load_dotenv

from pprint import pprint

load_dotenv()  # Loads .env file

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Create a client
supabase: Client = create_client(url, key)


def get_client() -> Client:
    return supabase
