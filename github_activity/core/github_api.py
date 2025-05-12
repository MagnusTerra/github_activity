import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubApi:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
            "Accept": "application/vnd.github.v3+json",
        }

    def get_user(self, username):
        response = requests.get(f"{self.base_url}/users/{username}", headers=self.headers)
        return response.json()

    def get_user_events(self, username):
        response = requests.get(f"{self.base_url}/users/{username}/events", headers=self.headers)
        return response.json()

    def get_user_repos(self, username):
        response = requests.get(f"{self.base_url}/users/{username}/repos", headers=self.headers)
        return response.json()