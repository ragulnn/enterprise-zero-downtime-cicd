# Phase 0 - Repository Setup

## Objective

In this phase, we initialize our project repository and prepare the folder structure that will be used throughout the project.

---

# Learning Objectives

By the end of this phase, you should understand:

- What Git is
- What GitHub is
- How Git stores project history
- How to clone a repository
- How to commit code
- How to push code
- Why we organize projects into folders
- Basic Git workflow

---

# What is Git?

Git is a Version Control System (VCS).

It tracks every change made to your project.

Instead of saving files like

```
project-final
project-final2
project-final-real
project-final-final
project-final-final-new
```

Git stores every version automatically.

Think of Git as a time machine for your code.

---

# What is GitHub?

GitHub is a cloud platform that hosts Git repositories.

Git manages your project locally.

GitHub stores it online.

Architecture:

```
Your Laptop
      │
      ▼
Git
      │
      ▼
GitHub
```

GitHub allows:

- Backup
- Collaboration
- Version history
- Pull Requests
- CI/CD integration

---

# Creating the Repository

Repository Name

```
enterprise-zero-downtime-cicd
```

Description

```
Production-grade CI/CD platform on Azure Kubernetes Service featuring zero-downtime deployments, Terraform infrastructure, Azure DevOps pipelines, Helm, Argo Rollouts, Prometheus, Grafana, DevSecOps, and automated rollback.
```

Visibility

```
Public
```

Reason:

Recruiters can view the project.

---

# Clone Repository

Command

```bash
git clone https://github.com/<username>/enterprise-zero-downtime-cicd.git
```

Explanation

```
git
```

Runs Git.

```
clone
```

Downloads a repository.

```
https://...
```

Repository location.

Move inside the project

```bash
cd enterprise-zero-downtime-cicd
```

Explanation

```
cd
```

Means Change Directory.

Verify

```bash
pwd
```

Lists your current folder.

---

# Creating the Folder Structure

Why?

Large projects become difficult to maintain if everything is stored in one folder.

We separate each responsibility.

```
app/
```

Application source code.

```
docker/
```

Dockerfiles.

```
terraform/
```

Infrastructure as Code.

```
helm/
```

Helm charts.

```
azure-pipelines/
```

Azure DevOps YAML pipelines.

```
monitoring/
```

Prometheus, Grafana, Alertmanager.

```
docs/
```

Project documentation.

```
scripts/
```

Automation scripts.

```
architecture/
```

Architecture diagrams.

---

# Important Files

README.md

Main project documentation.

LICENSE

Project license.

.gitignore

Files Git should ignore.

CHANGELOG.md

Project release history.

---

# Git Ignore

Purpose

Some files should never be uploaded.

Examples

- Virtual environments
- Terraform state
- Secrets
- Logs
- Cache files

These are listed in

```
.gitignore
```

---

# First Commit

Stage files

```bash
git add .
```

Explanation

```
git
```

Runs Git.

```
add
```

Adds files to the staging area.

```
.
```

Means "everything in the current directory."

---

Commit

```bash
git commit -m "chore: initialize enterprise zero downtime project"
```

Explanation

```
commit
```

Creates a snapshot.

```
-m
```

Allows a commit message.

```
chore
```

A conventional commit type used for setup or maintenance work.

---

# Pushing to GitHub

Command

```bash
git push -u origin main
```

Explanation

```
push
```

Uploads commits.

```
-u
```

Sets the upstream branch.

```
origin
```

Remote repository.

```
main
```

Main branch.

---

# Authentication Error

Error

```
remote: Invalid username or token.
Password authentication is not supported.
```

Reason

GitHub removed password authentication for Git operations.

Solution

Use SSH authentication.

Steps

1. Generate SSH key

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

2. Start SSH agent

```bash
eval "$(ssh-agent -s)"
```

3. Add key

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Display public key

```bash
cat ~/.ssh/id_ed25519.pub
```

5. Copy the output.

6. Open

```
https://github.com/settings/keys
```

7. Click

```
New SSH Key
```

8. Paste the key.

9. Change remote

```bash
git remote set-url origin git@github.com:<username>/enterprise-zero-downtime-cicd.git
```

10. Test

```bash
ssh -T git@github.com
```

11. Push

```bash
git push -u origin main
```

---

# Verify Everything

Check repository

```bash
git status
```

Expected

```
On branch main

nothing to commit
working tree clean
```

Check remote

```bash
git remote -v
```

Check commit history

```bash
git log --oneline
```

---

# Common Beginner Mistakes

## Forgot to enter the project folder

Check

```bash
pwd
```

---

## Wrong remote

Check

```bash
git remote -v
```

---

## Password authentication failed

Use SSH.

---

## Forgot to stage files

Run

```bash
git add .
```

---

## Nothing happens after commit

Remember

Commit saves locally.

Push uploads to GitHub.

---

# Git Workflow

```
Create Files

↓

git add .

↓

git commit

↓

git push

↓

GitHub Updated
```

---

# Interview Questions

### What is Git?

Git is a distributed version control system that tracks changes in source code.

---

### What is GitHub?

GitHub is a cloud platform that hosts Git repositories and enables collaboration.

---

### Difference between Git and GitHub?

Git is the tool.

GitHub is the hosting platform.

---

### What does git add do?

Moves changes into the staging area.

---

### What does git commit do?

Creates a snapshot of staged changes.

---

### What does git push do?

Uploads local commits to the remote repository.

---

### Why use SSH instead of HTTPS?

SSH provides secure authentication using public and private keys without requiring passwords for every push.

---

# Phase Completion Checklist

- Repository created
- Folder structure created
- Documentation added
- Git initialized
- First commit created
- SSH configured
- Repository pushed to GitHub

Phase 0 Complete ✅
