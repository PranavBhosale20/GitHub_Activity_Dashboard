# This will contain reusable functions to interact with the GitHub API
import requests

def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()
