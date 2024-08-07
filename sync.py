import os
import subprocess
import urllib.parse

def exec(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Couldnt {command}")
        print(result.stderr)
    return result.stdout

def sync(repo_url, target_dir):
    if not os.path.exists(target_dir):
        print(f"Cloning repo {repo_url} into {target_dir}")
    else:
        print(f"Pulling latest changes in {target_dir}")
        if not os.path.exists(os.path.join(target_dir, '.git')):
            print(f"The directory {target_dir} is not a git repository.")
            return
        current_dir = os.getcwd()
        os.chdir(target_dir)
        os.chdir(current_dir)

def main():
    username = "USERNAME"
    token = "GITHUB TOKEN TO ACCESS PRIVATE REPOS"

    # URL encode the token to handle special characters
    token = urllib.parse.quote(token, safe='')

    repo_url = f"https://{username}:{token}@github.com/{username}/Obsidian.git"  # url HAS to end with .git
    target_dir = "local/dir -> make sure slashes are /"

    sync(repo_url, target_dir)

if __name__ == "__main__":
    main()

   
