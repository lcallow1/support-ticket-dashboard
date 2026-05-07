from dotenv import load_dotenv
import os
import requests

load_dotenv()#Loads .env file

tenant_url = os.environ.get("HALO_TENANT_URL")
client_id = os.environ.get("HALO_CLIENT_ID")
client_secret = os.environ.get("HALO_CLIENT_SECRET")


def get_token():
    token_url = tenant_url + "/auth/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "all",
    }

    response = requests.post(token_url, data=payload)

    token = response.json()["access_token"]
    return token


def get_agents():
    token = get_token()

    agent_url = tenant_url + "/api/Agent"

    headers = {"Authorization": "Bearer " + token}
    response = requests.get(agent_url, headers=headers, params={"includeenabled": True})

    data = response.json()
    
    agents = {}
    for t in data:
        agents[t["id"]] = t["name"]

    return agents



def get_tickets(agents):
    token = get_token()

    ticket_url = tenant_url + "/api/Tickets"

    headers = {"Authorization": "Bearer " + token}#Authorises me
    response = requests.get(ticket_url, headers=headers, params={"open_only": True})

    data = response.json()
    halopsa_tickets = data["tickets"] if isinstance(data, dict) else data

    clean_tickets = []
    for t in halopsa_tickets:
        if t["tickettype_id"] == 1:#If ticket is suppport and not a project
            clean_tickets.append(
            {
                "id": t["id"],
                "title": t["summary"],
                "description": t["details"],
                "customer_name": t["user_name"],
                "agent_id": None if t["agent_id"] == 1 else t["agent_id"],#Making None relate to unnassigned instead of 1
                "created_at": t["dateoccurred"],
                "status_id": t["status_id"],
                "agent_name": agents.get(t["agent_id"], "Unassigned")
            }
        )

    return clean_tickets#Tickets with just the data I want

