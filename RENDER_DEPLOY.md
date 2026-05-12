# Deploy to Render (Free Tier)

## Quick Deploy

1. **Sign up:** https://render.com (GitHub login)

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo: `umarranginwala/ai-ml-portfolio`
   - Configure:
     - **Name:** oral-cancer-detection
     - **Root Directory:** `demo/oral-cancer-detection-demo`
     - **Runtime:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`

3. **Set Environment Variables:**
   - Add `SECRET_KEY` (any random string)

4. **Deploy!**
   - Click "Create Web Service"
   - Wait for build (~5 minutes)

**Your URL:** `https://oral-cancer-detection.onrender.com`

---

## 📋 Important: Git LFS

The model file (128MB) uses Git LFS. Render should handle this automatically when cloning.

If not, add this to render.yaml:
```yaml
services:
  - type: web
    name: oral-cancer-detection
    env: python
    buildCommand: |
      git lfs fetch
      pip install -r requirements.txt
    startCommand: gunicorn app:app
```

---

## 🆓 Render Free Tier Limits

- 512 MB RAM (enough for our app)
- Sleeps after 15 min idle (wakes on next request)
- 100 GB bandwidth/month

---

## 🔗 Quick Links

- **Render Dashboard:** https://dashboard.render.com
- **Your App:** https://oral-cancer-detection.onrender.com (after deploy)

---

## ⚠️ Alternative: PythonAnywhere

If Render doesn't work, try PythonAnywhere:
- Free forever (no sleep)
- Manual upload via web interface
- https://www.pythonanywhere.com
