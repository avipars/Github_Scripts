# TODO work on a more efficient way of getting this data 
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") 

# GitHub API endpoint for repositories
REPO_API_URL = "https://api.github.com/user/repos"

def get_few_repos(pages = 2):
    """Fetch a few repositories for the authenticated user."""
    repos = []
    page = 1

    while page <= pages:
        response = requests.get(REPO_API_URL, auth=(GITHUB_USERNAME, GITHUB_TOKEN), params={"page": page, "per_page": 100}, timeout=10)
        if response.status_code != 200:
            print("Error fetching repositories:", response.json())
            break

        data = response.json()
        if not data:  # No more repositories
            break

        repos.extend(data)
        page += 1

    return repos

def check_actions_enabled(repo):
    """Check if GitHub Actions is enabled for a repository."""
    actions_url = f"https://api.github.com/repos/{repo['full_name']}/actions/workflows"
    response = requests.get(actions_url, auth=(GITHUB_USERNAME, GITHUB_TOKEN), timeout=10)

    if response.status_code == 200:
        workflows = response.json().get("workflows", [])
        active_workflows = [wf for wf in workflows if wf.get("state") == "active"]
        return len(active_workflows) > 0
    else:
        print(f"Error checking actions for {repo['full_name']}: {response.json()}")
        return False

def main():
    print("Fetching some repositories...")
    repos = get_few_repos()

    print(f"Found {len(repos)} repositories. Checking for active GitHub Actions...")
    for repo in repos:
        if check_actions_enabled(repo):
            print(f"Active GitHub Actions found in: {repo['full_name']} {repo}")
            with open("active_actions.txt", "a", encoding="utf-8") as f: # report in txt file with repo name, and repo url
                f.write(f"Active GitHub Actions found in: {repo['full_name']}\n")
                f.write(f"Repo URL: {repo['html_url']} {repo} \n\n")
                

if __name__ == "__main__":
    main()
