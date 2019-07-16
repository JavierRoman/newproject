from github import Github
import json, sys

if __name__ == "__main__":
    args = sys.argv[1:]

    with open('/usr/local/bin/access_token.json') as json_file:
        json_data = json.load(json_file)

    g = Github(json_data['access_token'])
    user = g.get_user()
    user.get_repo(args[0]).delete()

