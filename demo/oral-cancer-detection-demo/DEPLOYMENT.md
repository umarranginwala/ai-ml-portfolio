# Deployment Options

This Flask app can be deployed to multiple platforms for public URL access.

## 🚀 Option 1: Heroku (Recommended)

**URL:** `https://oral-cancer-detection-ai.herokuapp.com`

### Setup Steps:

1. **Create Heroku Account**
   - Sign up at https://signup.heroku.com

2. **Install Heroku CLI**
   ```bash
   brew install heroku
   ```

3. **Login & Create App**
   ```bash
   heroku login
   heroku create oral-cancer-detection-ai
   ```

4. **Add GitHub Action Secret**
   - Go to GitHub Repo → Settings → Secrets → Actions
   - Add `HEROKU_API_KEY` (get from https://dashboard.heroku.com/account)

5. **Push to Deploy**
   ```bash
   git push origin main
   ```
   GitHub Actions will auto-deploy!

---

## 🌐 Option 2: PythonAnywhere (Free Forever)

**URL:** `https://umarranginwala.pythonanywhere.com`

### Setup Steps:

1. **Sign Up**
   - https://www.pythonanywhere.com

2. **Upload Code**
   - Use their web interface to upload files
   - Or use `git clone` in their console

3. **Configure WSGI**
   - Edit WSGI file to point to `app.py`
   - Set `application = app`

4. **Reload Web App**
   - Click the green reload button

---

## 🎯 Option 3: Render (Free Tier)

**URL:** `https://oral-cancer-detection.onrender.com`

### Setup Steps:

1. **Sign up** at https://render.com
2. **Connect GitHub repo**
3. **Create Web Service**
   - Root Directory: `demo/oral-cancer-detection-demo`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

---

## ⚡ Quick Start

**For immediate testing locally:**
```bash
cd demo/oral-cancer-detection-demo
python app.py
```
Open http://localhost:5000

**For public URL:** Choose one option above and follow steps.

---

## 📊 Platform Comparison

| Platform | Price | Ease | Sleep Mode | Best For |
|----------|-------|------|------------|----------|
| **Heroku** | Free | Easy | Yes (30s wake) | Quick demos |
| **PythonAnywhere** | Free | Medium | No | Always-on free hosting |
| **Render** | Free | Easy | Yes | Modern alternative |

---

## 🔧 Common Issues

**Git LFS on Heroku:**
- Add `heroku buildpacks:add https://github.com/raxod502/heroku-buildpack-git-lfs`

**Model Loading:**
- Ensure `model/oral_cancer_model.h5` or `.keras` is in the repo

**Memory Limits:**
- Free tiers have RAM limits (512MB-1GB)
- The model loads once at startup (~150MB)

---

## 📞 Support

Need help deploying? 
- Heroku docs: https://devcenter.heroku.com
- PythonAnywhere forums: https://www.pythonanywhere.com/forums/

---

**Recommendation:** Start with **Heroku** - easiest setup, automatic deployments from GitHub!
