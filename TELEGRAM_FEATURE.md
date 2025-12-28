# 📱 NEW: Telegram Bot Integration!

## Control Your Airdrop Bot from Your Phone! 🚀

The bot now supports **Telegram integration** for mobile control and instant notifications!

### 🎯 What You Get:

✅ **Mobile Control** - Run bot from anywhere via Telegram  
✅ **Instant Notifications** - Get alerts on your phone  
✅ **Simple Commands** - Just type `/claim` to get links  
✅ **24/7 Operation** - Bot runs even when computer is off  
✅ **Real-time Updates** - Live airdrop status  

### ⚡ Quick Setup (5 Minutes):

```bash
# 1. Install Telegram library (already in requirements.txt)
pip install -r requirements.txt

# 2. Create bot with @BotFather on Telegram
# Get your bot token

# 3. Add token to config.json
{
  "telegram_bot_token": "YOUR_BOT_TOKEN",
  "telegram_chat_id": "YOUR_CHAT_ID"
}

# 4. Run Telegram bot
python telegram_bot.py
```

### 💬 Available Commands:

| Command | What It Does |
|---------|-------------|
| `/start` | Welcome & menu |
| `/scan` | Find new airdrops |
| `/claim` | Get claim links |
| `/status` | Check airdrops |
| `/stats` | View earnings |
| `/remind` | Daily reminders |

### 📱 Example Usage:

```
You: /claim

Bot: 🎯 CLAIM THESE AIRDROPS NOW!

     1. T-Rex
        🔗 trex.xyz
        💰 1170 points

     2. PrismaX
        🔗 app.prismax.ai
        💰 1782 points

     [🚀 Claim T-Rex]
     [🚀 Claim PrismaX]
```

### 🔔 Auto Notifications:

Bot sends you daily reminders:
- **9:00 AM** - New airdrops found
- **10:30 AM** - Daily task reminder
- **Instant** - When new high-value airdrop detected

### 📚 Full Guide:

See **[TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)** for complete setup instructions!

---

## 🎯 Choose Your Mode:

### **Mode 1: Desktop Only**
```bash
python airdrop_hunter.py
```
- Run on computer
- Manual control
- Good for beginners

### **Mode 2: Telegram Bot** ⭐ (Recommended!)
```bash
python telegram_bot.py
```
- Mobile control
- Auto notifications
- 24/7 operation
- Best experience!

### **Mode 3: Both!**
```bash
# Terminal 1:
python telegram_bot.py

# Terminal 2:
python scheduler.py
```
- Maximum automation
- Desktop + Mobile
- Never miss anything!

---

## 🚀 Why Telegram Integration is Game-Changing:

### **Before:**
- ❌ Tied to computer
- ❌ Manual checking
- ❌ Miss notifications
- ❌ Limited access

### **After:**
- ✅ Control from phone
- ✅ Instant alerts
- ✅ Access anywhere
- ✅ 24/7 monitoring

---

## 📊 Comparison:

| Feature | Desktop Only | With Telegram |
|---------|-------------|---------------|
| **Mobile Control** | ❌ | ✅ |
| **Push Notifications** | ❌ | ✅ |
| **Remote Access** | ❌ | ✅ |
| **24/7 Operation** | ❌ | ✅ |
| **Ease of Use** | Medium | High |
| **Setup Time** | 5 min | 10 min |

---

## 🎉 Get Started:

1. **Basic Setup** (5 min):
   ```bash
   git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git
   cd crypto-airdrop-hunter-bot
   pip install -r requirements.txt
   python setup.py
   ```

2. **Add Telegram** (5 min):
   - Create bot with @BotFather
   - Add token to config.json
   - Run: `python telegram_bot.py`

3. **Start Earning!**
   - Send `/claim` on Telegram
   - Click links
   - Claim airdrops
   - Profit! 💰

---

**Full documentation in main [README.md](README.md)**

**Telegram setup guide: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)**

---

**⭐ Star this repo if Telegram integration helps you!** 🚀
