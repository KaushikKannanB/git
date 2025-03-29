## Commands Used:

### 1. Cloning the Repository:
```sh
git clone https://github.com/KaushikKannanB/git
```
- Clones the remote repository into the local machine.

### 2. Navigating and Creating Directories:
```sh
cd git
mkdir task3
cd task3
```
- Moves into the cloned repository and creates a new folder named `task3`.

### 3. Creating an Empty File:
```sh
echo >.gitkeep
```
- `.gitkeep` is used to track empty folders in Git.

### 4. Staging and Committing Changes:
```sh
git add task3/.gitkeep
git commit -m "Task 3 committed to remote"
```
- Adds and commits the `.gitkeep` file to track the empty `task3` folder.

### 5. Creating and Modifying a File:
```sh
echo k>third.txt
git add third.txt
git commit -m "third.txt committed"
```
- Creates a file `third.txt`, adds content, stages, and commits it.

### 6. Checking File Contents:
```sh
type third.txt
```
- Displays the content of `third.txt`.

### 7. Appending Content to a File:
```sh
echo kk>>third.txt
type third.txt
```
- Appends `kk` to `third.txt` and verifies it.

### 8. Restoring the Previous Committed State:
```sh
git restore third.txt
type third.txt
```
- Restores `third.txt` to its last committed state.

### 9. Discarding Uncommitted Changes:
```sh
git checkout -- third.txt
```
- Resets the file to the last committed version.

### 10. Checking Git Status:
```sh
git status
```
- Displays the current state of the working directory.

### 11. Committing Modified Files:
```sh
git add third.txt
git commit -m "Modified third.txt committed"
```
- Stages and commits the modified `third.txt` file.

### 12. Viewing Commit History:
```sh
git log --oneline
```
- Shows a concise log of commits.

### 13. Reverting a Commit:
```sh
git revert --no-edit <commit-hash>
```
- Reverts the specified commit without editing the commit message.

### 14. Resetting to a Previous Commit (Soft Reset):
```sh
git reset <commit-hash>
```
- Moves the branch pointer but keeps changes in the working directory.

### 15. Hard Reset to a Previous Commit:
```sh
git reset --hard <commit-hash>
```
- Moves the branch pointer and removes changes in the working directory.

### 16. Final Commit and Pushing Changes:
```sh
git add .
git commit -m "Worked out all, reset done, third.txt reverted back to initial state"
git push origin main
```
- Stages, commits, and pushes the final changes to the remote repository.

