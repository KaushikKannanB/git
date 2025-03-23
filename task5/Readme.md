
# Git Rebase Practice  

This document outlines the steps followed while practicing `git rebase` and explains their significance.  

## **Steps and Explanation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/KaushikKannanB/git
cd git
```
**Significance:**  
Cloning ensures we work on the latest version of the repository.  

---

### **2. Create a New Folder and Add a File**  
```sh
mkdir task5
cd task5
echo farewell > t.txt
git add .
git commit -m "Added t.txt in Task 5 folder"
```
**Significance:**  
- Created a new directory (`task5`).  
- Added a file (`t.txt`) and committed it.  

---

### **3. Check Commit History**  
```sh
git log --oneline
```
**Significance:**  
This command lists commit history in a compact form to track changes.  

---

### **4. Start an Interactive Rebase (Squash, Edit, Reorder Commits)**  
```sh
git rebase -i HEAD~5
```
- **Squash (`s`)** – Merge multiple commits into one.  
- **Edit (`e`)** – Modify a commit message.  
- **Reorder commits** by changing the order in the editor.  

**Significance:**  
- Helps keep a cleaner, more structured commit history.  
- Reduces unnecessary commits by squashing related changes.  

---

### **5. Amend a Commit Message**  
```sh
git commit --amend -m "Updated commit message"
git rebase --continue
```
**Significance:**  
- Modifies the last commit message if needed.  

---

### **6. Abort Rebase (If Needed)**  
```sh
git rebase --abort
```
**Significance:**  
- Cancels the rebase and restores the original commit history if something goes wrong.  

---

### **7. Push Changes to Remote**  
```sh
git push origin main
```
If push is rejected due to rebase history changes, force push:  
```sh
git push --force origin main
```
**Significance:**  
- Regular `git push` works if no history rewriting occurs.  
- **Force push (`--force`) is required after rebase** since it rewrites commit history.  

---

### **8. Verify Commit History**  
```sh
git log --oneline
```
**Significance:**  
- Ensures that the commit history reflects the intended changes.  

---

### **Conclusion**  
Using `git rebase`, we:  
✅ Squashed commits to keep history clean.  
✅ Edited commit messages to be more meaningful.  
✅ Reordered commits to maintain logical flow.  
✅ Successfully pushed the changes after rebase.  

---
