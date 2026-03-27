# 🚀 Deployment Guide - STI Knowledge Research Dashboard

## Step-by-Step Deployment to Streamlit Cloud

### Prerequisites:
- GitHub account (free at https://github.com)
- The files in this folder

---

## **STEP 1: Create GitHub Repository**

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `sti-knowledge-dashboard` (or any name)
   - **Description:** "Interactive STI Knowledge Research Dashboard"
   - **Public** (select this so Streamlit Cloud can access it)
3. Click "Create repository"
4. Copy the repository URL (something like `https://github.com/YOUR_USERNAME/sti-knowledge-dashboard.git`)

---

## **STEP 2: Push Your Code to GitHub**

Open PowerShell in the graphs folder and run:

```powershell
# Set your Git config (one time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: STI Knowledge Dashboard"

# Add remote (paste your copied URL)
git remote add origin https://github.com/YOUR_USERNAME/sti-knowledge-dashboard.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## **STEP 3: Deploy on Streamlit Cloud**

1. Go to https://streamlit.io/cloud
2. Click "Sign Up" → use your GitHub account
3. Click "New app"
4. Fill in:
   - **GitHub account:** Your GitHub username
   - **Repository:** `sti-knowledge-dashboard` (or your repo name)
   - **Branch:** `main`
   - **File:** `app.py`
5. Click "Deploy"

**DONE!** 🎉 Streamlit will give you a public URL like:
```
https://sti-knowledge-dashboard.streamlit.app
```

---

## **STEP 4: Share with Your Group**

Send them the Streamlit Cloud URL. They can:
- ✅ View the dashboard
- ✅ Use filters
- ✅ Download data
- ✅ See all visualizations and computations

---

## **Troubleshooting**

### If deployment fails:
1. Make sure `requirements.txt` is in the repository
2. Make sure `app.py` is at the root level
3. Check GitHub repo is set to **Public**
4. Streamlit Cloud has a free tier with limits (12hr/day sleep after inactivity)

### To update the dashboard:
```powershell
# Make changes locally in app.py
# Then:
git add .
git commit -m "Updated visualization"
git push origin main

# Streamlit Cloud automatically redeploys!
```

---

## **Share the Link**

Once deployed, share this link in your group chat:
```
https://sti-knowledge-dashboard.streamlit.app
```

Everyone can access it anytime! 📊

---

**Questions?** Let me know and I can help troubleshoot!
