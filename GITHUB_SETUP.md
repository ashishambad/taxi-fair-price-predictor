# GitHub Setup

## 1. Create a GitHub repository

Create a new repository on GitHub, then copy its HTTPS URL.

## 2. Open a terminal in this folder

```bash
cd taxi_trip_pricing_project
```

## 3. Initialize Git

```bash
git init
git add .
git commit -m "Initial commit - taxi trip pricing prediction"
```

## 4. Connect your GitHub repository

Replace the URL below with your repository URL:

```bash
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## 5. Streamlit deployment

In Streamlit Community Cloud, select this GitHub repository and use:

```text
app.py
```

as the application entry point.
