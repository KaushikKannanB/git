## 1. Creating and Switching Branches
```sh
 git checkout -b branch2
```
- This command creates a new branch named `branch2` and switches to it.

## 2. Creating a New Directory and Checking Git Status
```sh
mkdir task4
cd task4
git status
```
- `mkdir task4` creates a new directory named `task4`.
- `cd task4` navigates into the `task4` directory.
- `git status` checks the current branch and lists untracked files.

## 3. Creating and Adding a File to Git
```sh
echo creating conflict > t4.txt
git add t4.txt
git commit -m "Added t4.txt to task4 in branch2"
```
- `echo creating conflict > t4.txt` creates a file named `t4.txt` with content.
- `git add t4.txt` stages the file for commit.
- `git commit -m "Added t4.txt to task4 in branch2"` commits the file to the repository.

## 4. Switching to Another Branch and Modifying a File
```sh
git checkout branch1
echo adding this line for a conflict in another branch >> t4.txt
git add .
git commit -m "Appended a line in t4.txt to task4 in branch1"
```
- `git checkout branch1` switches to the `branch1` branch.
- `echo adding this line for a conflict in another branch >> t4.txt` appends text to `t4.txt`.
- `git add .` stages all modified files.
- `git commit -m "Appended a line in t4.txt to task4 in branch1"` commits the changes.

## 5. Viewing Git Log
```sh
git log --oneline
git log branch2 --oneline
```
- `git log --oneline` displays the commit history in a compact format.
- `git log branch2 --oneline` shows the commit history for `branch2`.

## 6. Merging Branches and Resolving Conflicts
```sh
git checkout branch1
git merge branch2
```
- `git checkout branch1` switches to `branch1`.
- `git merge branch2` attempts to merge `branch2` into `branch1`, leading to a conflict.

### Resolving the Conflict
```sh
git add .
git commit -m "Resolved the created conflict and merge"
```
- `git add .` stages resolved conflict files.
- `git commit -m "Resolved the created conflict and merge"` commits the merge resolution.

## 7. Viewing the Git Graph
```sh
git log --oneline --graph --all
```
- Shows a graphical representation of branches and commits.

## 8. Pushing Changes to Remote Repository
```sh
git push origin branch1
git push origin branch2
git push origin main
```
- `git push origin branch1` pushes `branch1` to the remote repository.
- `git push origin branch2` pushes `branch2` to the remote repository.
- `git push origin main` attempts to push `main` but fails due to remote changes.

### Force Pushing to Main
```sh
git push -f origin main
```
- `git push -f origin main` forcefully updates `main`, overwriting any conflicting history.

## 9. Final Verification
```sh
git log --oneline
```
- Displays the commit history after all merges and pushes.


