from supabase import Client
from postgrest.types import JSON
from db import get_client


client: Client = get_client()

def insert_inward(company, dc_no, po_no, heat_no):
    client.table("inward").insert({ "inw_comp": company, "inw_dc_no": dc_no, "inw_po_no": po_no, "inw_heat_no": heat_no }).execute()


def get_all_inwards() -> list[JSON]:
    all_inwards = client.table("inward").select("*").execute()
    return all_inwards.data





