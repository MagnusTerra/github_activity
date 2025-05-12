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
        result = response.json()
        return {
            "name": result["name"],
            "url": result["html_url"],
            "description": result["description"] if "description" in result else None,
            "created_at": result["created_at"],
            "updated_at": result["updated_at"],
            "pushed_at": result["pushed_at"] if "pushed_at" in result else None,
            "stargazers_count": result["stargazers_count"] if "stargazers_count" in result else None,
            "watchers_count": result["watchers_count"] if "watchers_count" in result else None,
            "forks_count": result["forks_count"] if "forks_count" in result else None,
            "open_issues_count": result["open_issues_count"] if "open_issues_count" in result else None,
            "license": result["license"]["name"] if "license" in result else None,
        }

    def get_user_events(self, username):
        response = requests.get(f"{self.base_url}/users/{username}/events", headers=self.headers)
        result = []
        
        for event in response.json():
            event_type = event["type"]
            repo_name = event["repo"]["name"]
            payload = event.get("payload", {})
            
            if event_type == "PushEvent":
                # For push events, count the number of commits
                commit_count = len(payload.get("commits", []))
                if commit_count > 0:
                    result.append(f"Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {repo_name}")
            
            elif event_type == "IssuesEvent" and payload.get("action") == "opened":
                # For issue events
                result.append(f"Opened a new issue in {repo_name}")
                
            elif event_type == "WatchEvent" and payload.get("action") == "started":
                # For star events
                result.append(f"Starred {repo_name}")
                
        return result

    def get_user_repos(self, username):
        response = requests.get(f"{self.base_url}/users/{username}/repos", headers=self.headers)
        result = []
        for repo in response.json():
            result.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"],
                "pushed_at": repo["pushed_at"],
                "stargazers_count": repo["stargazers_count"],
                "watchers_count": repo["watchers_count"],
                "forks_count": repo["forks_count"],
                "open_issues_count": repo["open_issues_count"],
                "license": repo["license"]["name"] if repo["license"] else None,
            })
        return result