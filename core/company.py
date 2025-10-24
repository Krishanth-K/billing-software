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

def get_all_company() -> list[JSON]:
    all_comp = client.table("company").select("*").execute()
    return all_comp.data

def get_all_company_names() -> list[JSON]:
    all_name = client.table("company").select("comp_name").execute()
    return all_name.data


def validate_company(company_name) -> bool:
    all_names = get_all_company_names()

    if company_name in all_names[0].values():
        return True

    return False
