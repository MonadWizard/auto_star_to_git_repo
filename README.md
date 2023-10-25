# 🚀 GitHub Automation Scripts 🤖

Welcome to the GitHub Automation Scripts! We have two types of scripts here:

1. **Starstruck Script:** This script is all about spreading the love to your favorite GitHub user by starring (or "watching") all of their repositories.

2. **Unstar All the Things:** Feeling fickle? This script allows you to retract all the stars (or "unwatch") you've given to a specific GitHub user's repositories.

## Before We Begin

To kick off this coding adventure, you'll need to prepare a configuration file. It's like the secret recipe for our GitHub bots, and it has to be named: **config.json** 🤫.

Inside this JSON file, you need to fill in three key ingredients:

```json
{
    "github_username": "YourGitHubUsername",
    "personal_access_token": "YourPersonalAccessToken",
    "target_username": "TargetGitHubUsername"
}



** github_username: **  This is the username you use to login to GitHub.

** personal_access_token: ** To get this magic key, follow these enchanting steps:

**GitHub Access Configuration**

To enable your GitHub automation journey, you'll need to set up your GitHub access configuration. Here's how to create a Personal Access Token (PAT) and select your target user.

1. **GitHub Username:** Your GitHub username is the key to your GitHub realm. If you don't have one, create an account on the [GitHub website](https://github.com).

2. **Personal Access Token (PAT):** To obtain a PAT, follow these enchanted steps:

   a. **Log into GitHub:** Open your web browser and enter the magical GitHub realm. If you're not already logged in, use your GitHub wand to access your account.

   b. **Access Token Settings:** In the top-right corner of the GitHub realm, find your avatar. It's your gateway to GitHub's backstage. Click it and choose "Settings" from the drop-down menu.

   c. **Developer's Den:** Within the mystical GitHub Settings, scroll down and find "Developer settings." This is where GitHub wizards concoct their potions.

   d. **Craft a Personal Access Token:** In the Developer settings menu, locate "Personal access tokens."

   e. **Summon a New Token:** Click the "Generate token" button, much like creating a new spell.

   f. **Enchant Your Token:** Give your token a name, similar to naming your magical pet. Then, choose the scopes (permissions) for your token. Each scope is like a different spell in your spellbook. Select the ones you need for your GitHub wizardry.

   g. **Brew the Token:** After configuring your token, scroll down and click the "Generate token" button. You've just brewed a potion (in this case, a token).

   h. **Capture the Magic:** Once your token is born, it will appear on the screen. Here's the secret: GitHub will only show it to you once! So, copy the token and keep it safe in your GitHub spellbook (or your secret token vault).

   i. **Protect Your Magic:** Store your personal access token like it's the One Ring—it's powerful and should be kept hidden. Do not share it publicly or in your scripts. If you ever need to revoke or regenerate a token, you can do so in the "Personal access tokens" settings on GitHub.

3. **Target User Selection:** This is the GitHub username of the user whose repositories you want to interact with. Choose wisely, and always respect the GitHub community!

Now that your configuration is prepared, and your magical token is in hand, you're ready to embark on your GitHub automation journey.

Simply run your script for your desired action, and watch the magic happen! ✨

**Note:** Always be respectful of GitHub's policies and guidelines when automating actions on the platform. Happy scripting!


Just run the script for your desired action, and watch the magic happen! ✨

Note: Always be respectful of GitHub's policies and guidelines when automating actions on the platform. Happy scripting!
