
## Step 1: Initialize a Local Repository
```sh
# Navigate to your project directory
cd sumo

# Initialize a new Git repository
git init

# Create a README file
echo  > t9.txt

# Stage and commit the changes
git add README.md
git commit -m "First commit in task9 added t9.txt"
```

## Step 2: Push to a Remote Repository
```sh
# Add the remote repository (replace with your actual repository URL)
git remote add origin https://github.com/KaushikKannanB/git

# Rename the default branch to main
git branch -M task9branch

# Push the local repository to the remote
git push -u origin task9branch
```

## Step 3: Create a Feature Branch
```sh
# Create and switch to a new feature branch
git checkout -b branch3

# Make changes to files, then stage and commit them
git add README.md
git commit -m "Updated t9.txt"

# Push the branch to the remote repository
git push -u origin branch3
```

![image](https://github.com/user-attachments/assets/14744fb1-be9a-407e-8738-dc78f42a4520)

![image](https://github.com/user-attachments/assets/075fff8a-8221-4ab6-b128-f4f14e5503d4)

![image](https://github.com/user-attachments/assets/4ebb93b3-6285-491c-9239-7bc37ad16da4)

## Step 5: Delete branch3
```sh
# Ensure you are on the main branch
git checkout branch3

# Pull the latest changes from the remote repository
git pull origin --delete branch3
```



## Step 6: Pull the Changes Locally
```sh
# Ensure you are on the main branch
git checkout task9branch

# Pull the latest changes from the remote repository
git pull origin task9branch
```
