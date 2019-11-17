# Setting up git
git config --global user.name <your-username>
git config --global user.email <your-email>

# Creating a repository
git init (perform inside your repository)
git add . (add files to git tracking)
git commit -m "Your commit message here."

# Accessing your history
git log (to look back at commits)
git checkout <hash> (puts your HEAD at a specific previous commit)
git reset --hard <hash> (allows you to revert back to a previous commit, dangeous)

# Updating your branch and pushing
git merge master (bringing changes from master into your current branch)
git push -u <remote> <branch-name> (u flag sets branch.<name>.merge for the local-branch)
git pull (argumentless command looks at branch.<name>.merge to determine where to pull from)
git push -u origin master ~ git push origin master ; git branch --set-upstream master origin/master
To explicitly set this:
	git config branch.master.remote origin
	git config branch.master.merge refs/heads/master

Getting branched commits into master:
	git checkout -b <branch-name>
	git checkout master
	git merge <branch-name>
