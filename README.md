# 🚀 Crypto Airdrop Hunter Bot

Automated crypto airdrop discovery and claiming assistant. Find FREE airdrops, track tasks, and maximize your crypto earnings!

## ✨ Features

- 🔍 **Daily Airdrop Discovery** - Automatically finds latest high-value FREE airdrops
- 📊 **Smart Filtering** - Only legitimate projects with zero-cost entry
- 🔔 **Task Reminders** - Never miss daily tasks (PrismaX, T-Rex, Hotstuff, etc.)
- 🤖 **Browser Automation** - Auto-fill forms and complete social tasks
- 💰 **Value Tracking** - Estimates potential earnings from each airdrop
- 🛡️ **Scam Detection** - Filters out fake/malicious airdrops
- 📱 **Telegram Notifications** - Get alerts on your phone

## 🎯 Current Supported Airdrops

- **T-Rex** (trex.xyz) - Points + Badges system
- **PrismaX** (app.prismax.ai) - Daily login rewards
- **Hotstuff** - Testnet participation
- Auto-discovers new airdrops daily!

## 🔧 Installation

### Prerequisites
- Python 3.8+
- Chrome/Chromium browser
- MetaMask or Phantom wallet

### Setup

```bash
# Clone repository
git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git
cd crypto-airdrop-hunter-bot

# Install dependencies
pip install -r requirements.txt

# Configure settings
cp config.example.json config.json
# Edit config.json with your details
```

## ⚙️ Configuration

Edit `config.json`:

```json
{
  "wallet_address": "YOUR_WALLET_ADDRESS",
  "telegram_bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "telegram_chat_id": "YOUR_CHAT_ID",
  "twitter_username": "YOUR_TWITTER",
  "discord_username": "YOUR_DISCORD",
  "email": "YOUR_EMAIL",
  "scan_interval_hours": 24,
  "auto_claim": false
}
```

**IMPORTANT**: 
- ⚠️ Never share your private keys or seed phrases
- ⚠️ Set `auto_claim: false` for manual approval (RECOMMENDED)
- ⚠️ Use a separate wallet for airdrops

## 🚀 Usage

### Basic Mode (Safe - Recommended)
```bash
python airdrop_hunter.py
```
This will:
1. Scan for new airdrops
2. Send you notifications with links
3. You manually claim (SAFE!)

### Advanced Mode (Browser Automation)
```bash
python airdrop_hunter.py --auto-tasks
```
This will:
1. Auto-complete social tasks (Twitter follow, Discord join)
2. Auto-fill forms
3. Stop at wallet signing (you approve manually)

### Scheduled Mode
```bash
# Run daily at 9 AM
python scheduler.py
```

## 📋 Features Breakdown

### 1. Airdrop Scanner (`scanner.py`)
- Searches CryptoRank, Airdrops.io, Twitter
- Filters by: FREE, Active, Legitimate
- Extracts: Project name, value, tasks, links

### 2. Task Automator (`automator.py`)
- Browser automation with Selenium
- Auto-completes:
  - Twitter follows/likes
  - Discord joins
  - Form submissions
  - Daily check-ins
- **STOPS at wallet transactions** (you sign manually)

### 3. Notification System (`notifier.py`)
- Telegram alerts
- Email summaries
- Desktop notifications

### 4. Value Tracker (`tracker.py`)
- Tracks your points/tokens
- Estimates USD value
- Shows ROI (time vs potential earnings)

## 🛡️ Security Features

✅ **No Private Key Storage** - Never stores sensitive data
✅ **Manual Transaction Approval** - You control all wallet actions
✅ **Scam Detection** - Checks project legitimacy
✅ **Rate Limiting** - Prevents account bans
✅ **Separate Wallet Recommended** - Use dedicated airdrop wallet

## 📊 Example Output

```
🔍 Daily Airdrop Scan Results (28 Dec 2024)

✅ NEW AIRDROP FOUND!
Project: LayerZero V2
Value: ~$500-1000 (estimated)
Time: 20 minutes
Tasks: Bridge transactions, testnet activity
Link: https://layerzero.network
Status: CONFIRMED

✅ DAILY TASK REMINDER
PrismaX: Login now (+10 points) → app.prismax.ai
T-Rex: 3 new quests available → trex.xyz

💰 Your Stats:
Total Airdrops: 12
Completed Tasks: 156
Estimated Value: $2,450
Time Invested: 8.5 hours
```

## 🤝 Contributing

Pull requests welcome! Areas to improve:
- Add more airdrop sources
- Improve scam detection
- Add more chains (Solana, Base, etc.)
- Better value estimation

## ⚠️ Disclaimer

- **Use at your own risk** - Crypto airdrops are speculative
- **No guarantees** - Airdrop values can be $0
- **DYOR** - Always verify projects independently
- **Security first** - Never share private keys with anyone
- **Not financial advice** - This is educational software

## 📝 License

MIT License - Free to use and modify

## 🔗 Links

- [CryptoRank Airdrop Dashboard](https://cryptorank.io/drophunting)
- [Airdrops.io](https://airdrops.io)
- [T-Rex Official](https://trex.xyz)
- [PrismaX App](https://app.prismax.ai)

## 💬 Support

Issues? Questions? Open a GitHub issue or contact via Telegram.

---

**⭐ Star this repo if it helps you earn FREE crypto!**

Made with ❤️ for the airdrop community 🚀
