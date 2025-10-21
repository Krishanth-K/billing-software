from supabase import Client
from postgrest.types import JSON
from db import get_client


class Company:
    def __init__(self, name, address, gst_no, phone_no):
        self.name = name
        self.address = address
        self.gst_no = gst_no
        self.phone_no = phone_no


client: Client = get_client()

def get_all_companies() -> list[JSON]:
    all_comp = client.table("company").select("*").execute()
    return all_comp.data
