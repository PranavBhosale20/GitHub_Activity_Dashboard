# utils/github_api_handler.py

import requests

<<<<<<< HEAD
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
=======
def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    return response.json()

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repos: {response.status_code}")
    return response.json()
>>>>>>> a1755844eb7b6ead5f51a0fd6ec24d6b1c66f88a

