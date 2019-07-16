# Author: Javier Roman
# This scripts is used to create a new repository in github

from github import Github
import json, sys


if __name__ == "__main__":
    args = sys.argv[1:]

    with open('/usr/local/bin/access_token.json') as json_file:
        json_data = json.load(json_file)

    g = Github(json_data['access_token'])
    user = g.get_user()
    user.create_repo(args[0])
