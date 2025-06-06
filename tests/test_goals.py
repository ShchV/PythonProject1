import os
import requests
from dotenv import load_dotenv

from modules.goals_methods import create_goal, get_goal, update_goal, delete_goal

load_dotenv()
BASE_URL = "https://api.clickup.com/api/v2"
HEADERS = {
    "Authorization": os.getenv("CLICKUP_TOKEN"),
    "Content-Type": "application/json"
}
TEAM_ID = os.getenv("TEAM_ID")
USER_ID = int(os.getenv("USER_ID"))

def test_goal_with_wrong_token():
    url = f"{BASE_URL}/team/{TEAM_ID}/goal"
    res = requests.get(url, headers={"Authorization": "bad_token"})
    assert res.status_code in [401, 403]

def test_goal_valid_token():
    goal = create_goal()
    assert goal.status_code == 200
    goal_id = goal.json()["goal"]["id"]

    result = get_goal(goal_id)
    assert result.status_code == 200

    result = update_goal(goal_id)
    assert result.status_code == 200

    result = delete_goal(goal_id)
    assert result.status_code == 200
