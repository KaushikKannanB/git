
## **Steps Followed & Commands Used**

### **1. Clone the Repository**  
Cloning the remote repository to the local system.  
```sh
git clone https://github.com/KaushikKannanB/git
```


### **2. Navigate to the Cloned Repository**  
```sh
cd git
```

### **3. Create a New Directory and File**  
```sh
mkdir task6
cd task6
echo try stashing > stask.txt
```

### **4. Add File to Staging**  
```sh
git add .
git status
```
👉 **Purpose**: Adds `stask.txt` to the staging area and verifies its status.

### **5. Stash the Changes**  
```sh
git stash
```
👉 **Purpose**: Saves uncommitted changes temporarily and reverts the working directory to a clean state.

### **6. Verify Stashed Changes**  
```sh
git stash list
git stash show
```
👉 **Purpose**:  
- `git stash list`: Lists all stashed changes.  
- `git stash show`: Shows details of the most recent stash.

### **7. Switch to Another Branch**  
```sh
git checkout branch1
```
👉 **Purpose**: Moves to another branch (`branch1`) to work on something else.

### **8. Switch Back to the Main Branch**  
```sh
git checkout main
```
👉 **Purpose**: Returns to the `main` branch where changes were stashed.

### **9. Apply Stashed Changes**  
```sh
git stash apply
```
👉 **Purpose**: Restores the most recent stash without removing it from the stash list.

### **10. Remove the Stash After Applying**  
```sh
git stash pop
```
👉 **Purpose**: Applies the stash and removes it from the stash list.

### **11. Verify Restored Changes**  
```sh
git status
```
👉 **Purpose**: Ensures that the previously stashed file is now ready to be committed.

### **12. Commit the Stashed Work**  
```sh
git commit -m "Applied Stashing"
```
👉 **Purpose**: Saves the restored changes into the Git history.

### **13. Push the Changes to Remote Repository**  
```sh
git push origin main
``
