# 🚀 Deploy Your Telegram Bot (Live 24/7)

## Quick Deploy Options

### Option 1: Railway.app (Recommended - FREE)

**Step 1: Create Account**
1. Go to https://railway.app
2. Sign up with GitHub

**Step 2: Deploy**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose: `samarthkumar096-commits/crypto-airdrop-hunter-bot`
4. Railway will auto-detect and deploy!

**Step 3: Add Environment Variables**
1. Go to project settings
2. Click "Variables"
3. Add:
   ```
   TELEGRAM_BOT_TOKEN=8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY
   TELEGRAM_CHAT_ID=5428245719
   ```

**Step 4: Done!**
Bot will be live 24/7! 🎉

---

### Option 2: Heroku (FREE Tier)

**Step 1: Install Heroku CLI**
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

**Step 2: Login & Deploy**
```bash
heroku login
heroku create samarth-airdrop-bot
git push heroku main
```

**Step 3: Set Environment Variables**
```bash
heroku config:set TELEGRAM_BOT_TOKEN=8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY
heroku config:set TELEGRAM_CHAT_ID=5428245719
```

**Step 4: Start Bot**
```bash
heroku ps:scale web=1
```

---

### Option 3: Replit (Easiest!)

**Step 1: Import**
1. Go to https://replit.com
2. Click "Create Repl"
3. Select "Import from GitHub"
4. Paste: `https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot`

**Step 2: Add Secrets**
1. Click "Secrets" (lock icon)
2. Add:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: `8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY`
3. Add:
   - Key: `TELEGRAM_CHAT_ID`
   - Value: `5428245719`

**Step 3: Run**
1. Click "Run" button
2. Bot is live!

**Step 4: Keep Alive (24/7)**
1. Use UptimeRobot.com
2. Ping your Repl URL every 5 minutes
3. Bot stays alive 24/7!

---

### Option 4: PythonAnywhere (FREE)

**Step 1: Create Account**
1. Go to https://www.pythonanywhere.com
2. Sign up (free tier)

**Step 2: Clone Repo**
```bash
git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git
cd crypto-airdrop-hunter-bot
```

**Step 3: Install Dependencies**
```bash
pip3 install --user -r requirements.txt
```

**Step 4: Create config.json**
```json
{
  "telegram_bot_token": "8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY",
  "telegram_chat_id": "5428245719"
}
```

**Step 5: Run as Always-On Task**
1. Go to "Tasks" tab
2. Add: `python3 /home/yourusername/crypto-airdrop-hunter-bot/telegram_bot.py`
3. Set to run daily

---

## 🎯 Recommended: Railway.app

**Why?**
- ✅ Completely FREE
- ✅ Auto-deploys from GitHub
- ✅ 24/7 uptime
- ✅ Easy environment variables
- ✅ No credit card needed
- ✅ 500 hours/month free

**Setup Time:** 5 minutes

---

## 🔧 Environment Variables Needed

For any platform, you need these:

```
TELEGRAM_BOT_TOKEN=8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY
TELEGRAM_CHAT_ID=5428245719
```

---

## ✅ Verify Bot is Live

After deployment:

1. Open Telegram
2. Go to @samarth_airdrop_hunter_bot
3. Send `/start`
4. Bot should reply!

If bot replies = SUCCESS! 🎉

---

## 🐛 Troubleshooting

**Bot not responding?**
- Check logs on your platform
- Verify environment variables
- Make sure bot is running

**Railway Logs:**
```
Settings → Deployments → View Logs
```

**Heroku Logs:**
```bash
heroku logs --tail
```

---

## 📊 Monitor Bot

**Check if bot is running:**
- Railway: Dashboard shows "Active"
- Heroku: `heroku ps`
- Replit: Green dot on Repl
- PythonAnywhere: Tasks tab shows "Running"

---

## 🚀 Quick Start (Railway - Fastest)

```
1. Go to railway.app
2. Sign in with GitHub
3. New Project → Deploy from GitHub
4. Select: crypto-airdrop-hunter-bot
5. Add environment variables
6. Done! Bot is live! 🎉
```

**Total time: 5 minutes**

---

## 💡 Pro Tips

1. **Use Railway** - Easiest and most reliable
2. **Set up monitoring** - UptimeRobot for 24/7 uptime
3. **Check logs** - Monitor for errors
4. **Test regularly** - Send `/status` daily

---

**Need help? Open an issue on GitHub!**
