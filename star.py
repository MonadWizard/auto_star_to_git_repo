import requests
import json

# # Your GitHub username and personal access token
# github_username = "MonadWizard"
# personal_access_token = "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"

# # The GitHub username whose public repositories you want to star
# target_username = "MonadWizard"

# # Set up the request headers with your personal access token
# headers = {
#     "Authorization": f"token {personal_access_token}",
#     "Accept": "application/vnd.github.v3+json",
# }

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


# Define a function to star all public repositories of the target user
def star_all_public_repositories():
    # Define the GitHub API URL for listing public repositories of the target user
    api_url = f"https://api.github.com/users/{target_username}/repos?per_page=100&page="

    page = 1

    while True:
        # Send a GET request to the GitHub API
        response = requests.get(f"{api_url}{page}", headers=headers)

        if response.status_code == 200:
            repositories = response.json()

            # If there are no more repositories, exit the loop
            if not repositories:
                break

            # Star each repository
            for repo in repositories:
                star_url = f"https://api.github.com/user/starred/{target_username}/{repo['name']}"
                response = requests.put(star_url, headers=headers)
                if response.status_code == 204:
                    print(f"Starred {target_username}/{repo['name']}")
                else:
                    print(f"Failed to star {target_username}/{repo['name']}")

            page += 1
        else:
            print(
                f"Failed to fetch public repositories for {target_username}. Status code: {response.status_code}"
            )
            break


if __name__ == "__main__":
    star_all_public_repositories()
