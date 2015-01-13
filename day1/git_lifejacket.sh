
# Git Lifejacket
# ==============
# Git is a distributed version control system. What does that mean?
#
#   * Git makes it easy to share files (distributed).
#   * Git tracks the changes you make to files (version control system).
#
# Use git to...
#
#   1. Quickly distribute sets of files.
#   2. Keep multiple versions of a file without making copies.
#   3. Selectively undo changes you made 3 days or even 3 months ago.
#   4. Efficiently merge work from several different people.
#   5. ...
#
# This tutorial is a git lifejacket, meant to get you up and running.
#
# For more, see (try!) the git followup notes, posted online. Also check out 
# the git documentation at:
#
#     http://www.git-scm.com/doc
#
# You can also get help with commands by appending `--help` to the end. For
# example:
git status --help

# Git Repositories
# ================
# A git repository (or 'repo') is just a set of files tracked by git.
#
# GitHub.com is a host for git repositories on the web, widely-used by
# open-source projects. GitHub provides free hosting for public repositories.

# You might want to work on a repository someone else created. Download a copy
# of a repository from the web by cloning it:
#
#     git clone URL
#
git clone https://github.com/nick-ulle/2015-python.git

# Check the status of a repository with:
#
#     git status
#
git status

# You can also create new, empty repositories on GitHub, and then clone them:

git clone https://github.com/nick-ulle/demo.git

# Committing Changes
# ==================
# After changing some files, you can save a snapshot of the repository by
# making a commit. This is a 2 step process.

# Step 1:
#
# Add, or 'stage', the changes you want to save in the commit:
#
#     git add FILE
#
git add README.md

# To stage every file in the current repository:
#
#     git add --all

# Use `git status` to see which files are staged.

# Step 2:
#
# Save the staged changes with the command:
#
#     git commit
#
git commit

# The commit command will ask you to type a message summarizing the changes.
# The first line should be a short description, no more than 50 characters.
# If you want to write more, insert a blank line. For example:
#
#     Adds README.md, describing the repository.
#
#     The added README.md also contains a classic programming phrase and the
#     meaning of life, the universe, and everything.

# If you examine the repository status, git no longer sees any changes. This
# is because they've been committed.

# When should you make a commit?
#
# Common advice is to commit early and often. Commits are your save points,
# and you never know when you'll need to go back. You could commit every time
# you finish a small piece of work, such as writing a function.

# You can see a history of the last N commits with the command:
#
#     git log [-N]
#
git log
git log -3

# Your Turn!
# ==========
# Clone the demo repository from
#
#   https://www.github.com/nick-ulle/demo.git
#
# make a new file, type something in it, and commit the file.

# Working With Remote Repositories
# ================================
# What if you want to share your work online (say, GitHub)? An online
# repository is a 'remote' repository.

# Given permission (e.g., you own the repo), you can push commits to a remote
# repository with the command:
#
#     git push [REMOTE BRANCH]
#

# Push commits to the remote repo 'origin' on branch 'master':

git push origin master

# You can also retrieve commits other people have made to a repository. Do
# this with:
#
#     git pull [REMOTE BRANCH]
#
git pull origin master

