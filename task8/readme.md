
### Cloning the Repository
To clone the repository from GitHub, run:
```sh
git clone https://github.com/KaushikKannanB/git
```

Change into the cloned directory:
```sh
cd git
```

### Creating a New Directory
Create a new directory inside the project:
```sh
mkdir task8
```

### Installing Required Packages
Install `flake8` and `pytest` for linting and testing:
```sh
pip install flake8 pytest
```
> **Note:** If you encounter issues like *invalid distribution* warnings or installation errors, try fixing Python installation or running `pip install --force-reinstall flake8 pytest`.

### Creating Application Files
To create Python script files, open them in VS Code:
```sh
code app.py
```
Navigate to `task8` and create additional files:
```sh
cd task8
code app.py
code test_app.py
```

### Setting Up Pre-Commit Hook
Navigate to the `.git/hooks` directory:
```sh
cd ..
cd .git/hooks
```
Create a `pre-commit` file:
```sh
echo > pre-commit
notepad pre-commit
```
> Open `pre-commit` and add the following content to enforce `flake8` checks before commit:
```sh
#!/bin/sh

echo "Running flake8 for linting..."
flake8
if [ $? -ne 0 ]; then
    echo "Linting failed. Fix issues before committing."
    exit 1
fi
```
Save the file and ensure it is executable:
```sh
chmod +x .git/hooks/pre-commit
```

### Adding and Committing Changes
To add all files to staging:
```sh
git add .
```
Commit the changes:
```sh
git commit -m "Initial commit with pre-commit"
```
If the commit fails due to linting errors, resolve them before retrying.

### Running `flake8` Manually
If you face issues with `flake8` not being recognized, ensure it's installed correctly:
```sh
pip install --force-reinstall flake8
```
Check the version:
```sh
flake8 --version
```
Run `flake8` to check for errors:
```sh
flake8
```

### Fixing Linting Issues
Example errors:
```
.	ask8	est_app.py:1:1: F401 'pytest' imported but unused
.	ask8	est_app.py:4:1: E302 expected 2 blank lines, found 1
```
![Screenshot 2025-03-24 235848](https://github.com/user-attachments/assets/d25ad93c-960a-4940-b140-3f8221d862a5)
![Screenshot 2025-03-25 000000](https://github.com/user-attachments/assets/c35f4c67-b093-4835-a6bb-ae14cfa32cf7)
![Screenshot 2025-03-25 005614](https://github.com/user-attachments/assets/cc39441c-5a7b-47e1-851b-dc6cc899e042)



