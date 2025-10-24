from annotated_types import IsDigits
from supabase import Client
from postgrest.types import JSON

from db import get_client
from core.company import validate_company


client: Client = get_client()

def insert_inward(company, dc_no, po_no, heat_no):
    client.table("inward").insert({ "inw_comp": company, "inw_dc_no": dc_no, "inw_po_no": po_no, "inw_heat_no": heat_no }).execute()

def get_all_inwards() -> list[JSON]:
    all_inwards = client.table("inward").select("*").execute()
    return all_inwards.data


def validate_inward(company, dc_no, po_no, heat_no) -> bool:
    """
    Check if the details are correct before pushing to database
    """

    if not validate_company(company):
        print("Unknown company")
        return False

    if not dc_no.isdigit():
        return False
    if not po_no.isdigit():
        return False
    if not heat_no.isdigit():
        return False

    return True
