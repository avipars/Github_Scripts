import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # PAT Requires "Codespaces" repository permissions (read)
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
CODESPACES_API_URL = "https://api.github.com/user/codespaces" # GitHub API endpoint for Codespaces

def get_active_codespaces():
    """Fetch all active Codespaces for the authenticated user."""
    response = requests.get(CODESPACES_API_URL, auth=(GITHUB_USERNAME, GITHUB_TOKEN), timeout=10)
    
    if response.status_code == 200:
        codespaces = response.json().get("codespaces", [])
        return codespaces
    else:
        print(f"Error fetching Codespaces: {response.json()}")
        return []

def main():
    print("Fetching active Codespaces...")
    codespaces = get_active_codespaces()

    if not codespaces or len(codespaces) == 0:
        print("No active Codespaces found.")
        return

    print(f"Found {len(codespaces)} active Codespaces:")
    for codespace in codespaces:
        print(f"- Name: {codespace['name']}")
        print(f"  Repository: {codespace['repository']['full_name']}")
        print(f"  Repo URL: {codespace['repository']['html_url']}")
        print(f"  Web URL: {codespace['web_url']}")
        print(f"  Machine: {codespace['machine']['display_name']}")
        print(f"  State: {codespace['state']}")
        print(f"  Last Used: {codespace['last_used_at']}")
        print(f"  Location: {codespace['location']}")
        print("")
        # you could also just print 'codespace' to get everything in json format

if __name__ == "__main__":
    main()
