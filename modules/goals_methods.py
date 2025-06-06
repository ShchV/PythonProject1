import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.clickup.com/api/v2"
HEADERS = {
    "Authorization": os.getenv("CLICKUP_TOKEN"),
    "Content-Type": "application/json"
}
TEAM_ID = os.getenv("TEAM_ID")
USER_ID = int(os.getenv("USER_ID"))

def create_goal():
    my_headers = {
        "Authorization": "pk_188589815_B4AF250WLQVA3ZI5EK5LBV2ON4YQ5OHU",
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    body = {
        "name": "Test goal3",
        "due_date": "20260101",
        "description": "Test goal creation",
        "color": "blue",
        "multiple_owners": True,
        "owners": ["188589815"]
    }
    return requests.post(f"{BASE_URL}/team/{TEAM_ID}/goal", headers=my_headers, json=body)

def get_goal(goal_id):
    my_headers = {
        "Authorization": "pk_188589815_B4AF250WLQVA3ZI5EK5LBV2ON4YQ5OHU",
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    return requests.get(f"{BASE_URL}/goal/{goal_id}", headers=my_headers)

def update_goal(goal_id):
    my_headers = {
        "Authorization": "pk_188589815_B4AF250WLQVA3ZI5EK5LBV2ON4YQ5OHU",
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    body = {
        "name": "Test goal8",
        "due_date": "20260101",
        "description": "Test goal creation",
        "color": "blue",
        "multiple_owners": True,
        "owners": ["188589815"]
    }
    return requests.put(f"{BASE_URL}/goal/{goal_id}", headers=my_headers, json=body)

def delete_goal(goal_id):
    my_headers = {
        "Authorization": "pk_188589815_B4AF250WLQVA3ZI5EK5LBV2ON4YQ5OHU",
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    return requests.delete(f"{BASE_URL}/goal/{goal_id}", headers=my_headers)