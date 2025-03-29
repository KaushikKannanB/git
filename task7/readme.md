What is Git Cherry-Picking?
Cherry-picking in Git allows you to apply a specific commit from one branch to another without merging the entire branch. It is useful when you want to pick only one or a few commits from a different branch instead of merging all changes.

Use Case
Imagine you're working on a feature in branch1, and you make a commit that you realize should also be in main. Instead of merging all of branch1 into main, you can pick just that one commit and apply it to main.


## Cloning the Repository
```sh
git clone https://github.com/KaushikKannanB/git
```
- Clones the remote repository from GitHub to the local machine.
- In the first attempt, there was an RPC failure due to a connection reset.
- The second attempt was successful, and all objects were fetched.

## Navigating and Creating a Directory
```sh
cd git
mkdir task7
```
- `cd git` moves into the cloned repository.
- `mkdir task7` creates a new directory named `task7` within the repository.

## Checking Out a Branch
```sh
git checkout branch1
```
- Switches to `branch1`.
- Since `branch1` already exists on the remote, it is set up to track `origin/branch1`.

## Viewing Commit History
```sh
git log main --oneline
git log branch1 --oneline
```
- Displays commit history of `main` and `branch1` in a compact format.
- The `--oneline` flag shows each commit as a single line with its hash and message.

## Checking Repository Status
```sh
git status
```
- Displays the status of the working directory and staging area.
- Confirms that `branch1` is up to date with `origin/branch1`.

## Creating and Committing a New File
```sh
echo cherrypick attempt > t7.txt
git add .
git commit -m "Added t7.txt in task7 to branch1"
```
- `echo cherrypick attempt > t7.txt` creates a new file `t7.txt` with the content "cherrypick attempt".
- `git add .` stages all changes (new file `t7.txt`).
- `git commit -m "Added t7.txt in task7 to branch1"` commits the staged changes with the given message.

## Switching to Main Branch
```sh
git checkout main
```
- Switches from `branch1` to `main`.

## Cherry-Picking a Commit
```sh
git cherry-pick f3eb531
```
- Applies the commit `f3eb531` (which added `t7.txt` in `branch1`) to `main`.
- Ensures that `t7.txt` is included in `main` without merging the entire `branch1`.

## Verifying the Changes
```sh
git log --oneline
git log branch1 --oneline
```
- Checks that `t7.txt` has been added to `main` after cherry-picking.
- Confirms that the commit still exists in `branch1` as well.

