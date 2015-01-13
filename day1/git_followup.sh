
# More on Git
# ===========
# This file describes some everyday tasks in git.

# Creating Repositories
# =====================
# You don't have to use GitHub to create a new repository. You can create an
# new local repository named NAME with:
#
#     git init [NAME]
#
git init my-repo

# If you want to use a repository you created locally with a remote repository,
# you have to tell git where the remote repository is:
#
#     git remote [add NAME URL]
#

# Add a remote called origin:
git remote add origin https://github.com/nick-ulle/my-repo.git

# List all remotes for the current repo:
git remote

# After adding the remote repository, you can push and pull as usual.

# Branching
# =========
# Git supports keeping multiple working versions of a repository at once. These
# are represented as branches. Every repository starts with a branch called
# 'master'.
#
# To make a new branch named NAME, use:
#
#     git branch [NAME]
#
git branch experimental

# On its own, `git branch` will list the repository's branches:

git branch

# You can switch branches with:
#
#     git checkout NAME
#
git checkout experimental

# You can delete a branch with the following command:
#
#     git branch -d NAME
#
git checkout master
git branch -d experimental

git branch

# Now let's recreate that branch and switch to it.
git branch experimental
git checkout experimental

# If we make some changes on the branch and commit them, they don't get applied
# to any other branch.
touch testing.py
git add testing.py
git commit

ls
git log

git checkout master
ls
git log

git branch -v

# To merge commits from another branch into the current branch, use:
#
#     git merge BRANCH
#
git merge experimental

git status
git log
ls

# How should you use branches?
#
# Branches are useful for isolating experimental changes from code you already
# have working. They also make it easy to keep manage multiple drafts. 
#
# Use branches judiciously according to your own work habits, especially for
# projects where you're the only contributor. In larger, public projects, try
# to follow guidelines agreed upon by all the contributors.
#
# A popular branching workflow is described here:
#
#     http://nvie.com/posts/a-successful-git-branching-model/
#

# Stashing Changes
# ================
# You might want to switch branches, saving your work on the current branch
# without committing it. The solution to this is stashing:
#
#     git stash [pop]
#

# For example, suppose you add a Python file:
touch foo.py
git add foo.py

# Then you realize you want to switch branches and work on something completely
# different. Stash your current work to get it out of the way:
git stash

# Switch to a different branch and do other work, committing when you're done:
# (If you're following along, create the branch and switch to it with
#
#      git checkout -b branch
#
# )
git checkout other-branch

# When you're ready to go back to work on foo.py, you can switch back to the
# original branch and pop the stash:
git checkout master
git stash pop
ls

# Revising Commits
# ================
# What if you forget to add a change, make a typo in the commit message, etc?
# Fix it with:
#
#     git commit --amend
#
vim README.md
git add README.md
git commit --amend

# NEVER amend a commit you've already pushed to a remote repository. It will
# interfere with git's normal operation! Instead, you should make a new commit
# for any changes you forgot. 

# Restoring Previous Commits
# ==========================
# Since git tracks all of the commits you make, you can easily restore the
# state of the repository at an earlier point in time. You can do this with:
#
#     git reset COMMIT [FILE]
#
# where COMMIT is a commit hash (listed with `git log`). You only need
# to type the first few characters of the commit hash. For example:

git reset f4fca

# A more in-depth explanation of `git reset` is given in the git documentation.

