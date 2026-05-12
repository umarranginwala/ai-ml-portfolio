# Quick Deploy

## 🚀 One-Click Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click the button above to deploy instantly!

## Manual Deploy

```bash
# 1. Install Heroku CLI
brew install heroku

# 2. Login
heroku login

# 3. Create app
heroku create oral-cancer-detection-ai

# 4. Enable Git LFS support
heroku buildpacks:add https://github.com/raxod502/heroku-buildpack-git-lfs
heroku buildpacks:add heroku/python

# 5. Push to deploy
cd demo/oral-cancer-detection-demo
git push heroku main

# 6. Open app
heroku open
```

## 📊 Result

Your app will be live at:
**`https://oral-cancer-detection-ai.herokuapp.com`**

Users can:
1. Visit the URL
2. Upload oral cavity images
3. Get real-time AI predictions!

## ⚠️ Notes

- **Free tier sleeps after 30 min** - first visit takes ~30s to wake up
- **550 MB total size limit** (model + code fits within this)
- **Git LFS required** for the 128MB model file
