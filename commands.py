class Github:

    def __init__(self, bot):
        self.bot = bot  

    def get_user(self, username):
        return self.bot.get(f'https://api.github.com/users/{username}')
    def get_repos(self, username):
        return self.bot.get(f'https://api.github.com/users/{username}/repos')
    def how_to_commit(self):
        self.how_to_clone()
        print("git pull ")  # to recieve the latest file from the repository
        print("git add .")  # to add all the files to the staging area
        print("git status")  # to check the status of the files
        print("git commit -m 'message' ") # to commit the files with a message
        print("git push") # pushing the changed contents to repository 
         
    def how_to_clone(self):
        print("git clone <repository link>")
    
    def revert_commit(self):
        print("git log --oneline")  # to see the commit history
        print("git reset --hard <commit id>") # to go back to the previous commit

    def how_to_branch_new(self):
        print("git branch") # to see the list of branches
        print("git checkout -b <branch name>") # to switch to the new branch   
        print("git push origin <branch name>") # to push the new branch to the repository

    def switch_branch(self):
        print("git checkout <branch name>")

    def merge_branch(self):
        print("git merge <branch name>") # to merge the branch with the master branch

