import requests
import json

# Read credentials from the config file
with open("config.json") as config_file:
    config = json.load(config_file)

github_username = config["github_username"]
personal_access_token = config["personal_access_token"]
target_username = config["target_username"]

# Set up the request headers with your personal access token
headers = {
    "Authorization": f"token {personal_access_token}",
    "Accept": "application/vnd.github.v3+json"
}

# Define a function to unstar all repositories of the target user
def unstar_all_repositories():
    # Define the GitHub API URL for listing repositories the authenticated user has starred
    starred_url = f"https://api.github.com/user/starred"

    # Send a GET request to the GitHub API to get the list of starred repositories
    response = requests.get(starred_url, headers=headers)

    if response.status_code == 200:
        repositories = response.json()

        # Unstar each repository for the target user
        for repo in repositories:
            if repo["owner"]["login"] == target_username:
                unstar_url = f"https://api.github.com/user/starred/{target_username}/{repo['name']}"
                response = requests.delete(unstar_url, headers=headers)
                if response.status_code == 204:
                    print(f"Unstarred {target_username}/{repo['name']}")
                else:
                    print(f"Failed to unstar {target_username}/{repo['name']}")

    else:
        print(f"Failed to fetch starred repositories. Status code: {response.status_code}")

if __name__ == "__main__":
    unstar_all_repositories()
