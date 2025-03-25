
## Commands and Explanations

### 1. Cloning the Repository
```
git clone https://github.com/KaushikKannanB/git
```
**Purpose:** Clones the remote repository to the local machine.

---

### 2. Navigating into the Repository
```
cd git
```
**Purpose:** Changes the working directory to the newly cloned repository.

---

### 3. Checking the Current Status
```
git status
```
**Purpose:** Verifies the current branch and ensures the working directory is clean.

---

### 4. Creating a New Branch
```
git checkout -b task10branch
```
**Purpose:** Creates and switches to a new branch named `task10branch`.

---

### 5. Creating a New Directory and File
```
mkdir task10
cd task10
echo final git task > t10.txt
```
**Purpose:** Creates a new directory `task10`, navigates into it, and creates a text file `t10.txt` with sample content.

---

### 6. Viewing File Contents
```
type t10.txt
```
**Purpose:** Displays the content of `t10.txt` to confirm the file has the intended data.

---

### 7. Staging the File
```
git add .
```
**Purpose:** Stages all changes (in this case, `t10.txt`) to be committed.

---

### 8. Checking the Status After Staging
```
git status
```
**Purpose:** Confirms that `t10.txt` is staged for commit.

---

### 9. Committing the File
```
git commit -m "added t10.txt in task10 to task10branch"
```
**Purpose:** Saves the changes to the repository with a descriptive commit message.

---

### 10. Viewing the Commit History
```
git log --oneline
```
**Purpose:** Displays the commit history in a compact format.

---

### 11. Interactive Rebase to Modify the Last Two Commits
```
git rebase -i HEAD~2
```
**Purpose:** Starts an interactive rebase for the last two commits to modify the commit message.

---

### 12. Amending the Commit Message
```
git commit --amend -m "Updated commit message"
```
**Purpose:** Modifies the most recent commit message.

---

### 13. Continuing the Rebase
```
git rebase --continue
```
**Purpose:** Completes the rebase process after modifying the commit message.

---

### 14. Verifying the Changes
```
git log task10branch --oneline
```
**Purpose:** Checks the commit history to ensure the commit message was updated.

---

### 15. Pushing the Changes to the Remote Repository
```
git push origin task10branch
```
**Purpose:** Pushes the local `task10branch` to the remote repository.

---

### 16. Forcing the Push (If Required)
```
git push --force origin task10branch
```
**Purpose:** Ensures the pushed changes overwrite the remote branch if necessary.

---

### 17. Viewing the Reflog
```
git reflog
```
**Purpose:** Displays a log of recent Git actions, helping track commit history.

---

### 18. Recovering a Previous Commit
```
git checkout -b recoveredbranch 8d9ed72
```
**Purpose:** Creates a new branch (`recoveredbranch`) from the specified commit hash to restore previous changes.

---

### 19. Pushing the Recovered Branch
```
git push origin recoveredbranch
```
**Purpose:** Pushes the newly created `recoveredbranch` to the remote repository.

