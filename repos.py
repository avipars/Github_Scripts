
import requests
import os
from dotenv import load_dotenv


load_dotenv()
# Replace with your GitHub personal access token (provide it with necessary permissions) 
# Fine grained token: 
# Read access to metadata
# Read access to code, commit statuses, and pull requests
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME") 


# GitHub API URLs
BASE_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


def get_public_repos(username):
    """Get all public repositories for the user."""
    repos_url = f"{BASE_API_URL}/users/{username}/repos"
    repos = []
    page = 1

    while True:
        response = requests.get(repos_url, headers=HEADERS, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            print(f"Error fetching repos: {response.json()}")
            break
        data = response.json()
        if not data:
            break
        
        
        repos.extend(repo for repo in data if repo["owner"]["login"] == username and not repo["private"]) # Filter out private and not owner repositories
        page += 1

    return repos # you can change this line if you want less information for each repo for example to: # [repo["name"] for repo in repos] 
    
def main():
    print("Fetching all repositories...")
    repos = get_public_repos(GITHUB_USERNAME)

    print(f"Found {len(repos)} repositories.")
    for repo in repos:
       print(repo)
                

if __name__ == "__main__":
    main()
