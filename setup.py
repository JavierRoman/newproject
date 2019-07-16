import os, json

if __name__ == "__main__":
    github_username=input("Github username:")
    working_directory=input("Full working directory path:")

    if not os.path.exists(working_directory):
        os.mkdir(working_directory)

    with open("commands.config", "w") as f:
        f.write(github_username)
        f.write("\n")
        f.write(working_directory)

    access_token=input("Github access token:")

    with open("access_token.json", "w") as json_file:
        json.dump({"access_token": access_token}, json_file)