# utils/github_api_handler.py

import requests

BASE_URL = "https://api.github.com"

def get_user_profile(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_user_repos(username):
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

