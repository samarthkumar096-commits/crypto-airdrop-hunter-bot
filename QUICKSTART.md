# 🚀 Quick Start Guide

## Installation (5 minutes)

### Step 1: Install Python
Download Python 3.8+ from [python.org](https://www.python.org/downloads/)

### Step 2: Clone Repository
```bash
git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git
cd crypto-airdrop-hunter-bot
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure
```bash
cp config.example.json config.json
# Edit config.json with your details
```

### Step 5: Run Bot
```bash
python airdrop_hunter.py
```

## Usage Examples

### Interactive Mode (Recommended for Beginners)
```bash
python airdrop_hunter.py
```
Then select from menu:
- Option 2: View current airdrops
- Option 3: Run automation
- Option 4: Check value estimates

### Automated Mode (Set and Forget)
```bash
python scheduler.py
```
Runs automatically:
- 9:00 AM: Scans for new airdrops
- 10:30 AM: Daily task reminder
- Sunday 8 PM: Weekly report

### Manual Scan Only
```bash
python scanner.py
```

## Configuration

Edit `config.json`:

```json
{
  "wallet_address": "0xYourAddress",
  "email": "your@email.com",
  "twitter_username": "@yourusername"
}
```

**IMPORTANT**: 
- Use a SEPARATE wallet for airdrops
- NEVER share private keys
- Set `auto_claim: false` (default)

## Current Airdrops

### 1. T-Rex (trex.xyz)
- **Time**: 33 minutes
- **Value**: 1170 points
- **Tasks**: Sign up, badges, quests

### 2. PrismaX (app.prismax.ai)
- **Time**: 11 minutes
- **Value**: 1782 points
- **Tasks**: Daily login

### 3. Hotstuff
- **Time**: 10 minutes
- **Value**: 1265 points
- **Tasks**: Testnet participation

## Safety Tips

✅ **DO**:
- Use separate airdrop wallet
- Verify all links manually
- Keep private keys offline
- Research projects before participating

❌ **DON'T**:
- Share private keys/seed phrases
- Send ETH/tokens to claim airdrops
- Trust "guaranteed" airdrops
- Use your main wallet

## Troubleshooting

### Browser doesn't open
```bash
# Install Chrome driver
pip install webdriver-manager
```

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Config not found
```bash
# Copy example config
cp config.example.json config.json
```

## Support

- GitHub Issues: [Report bugs](https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot/issues)
- Discussions: Share tips and strategies

## Next Steps

1. ⭐ Star this repo
2. 🔔 Watch for updates
3. 🤝 Contribute improvements
4. 💰 Start claiming airdrops!

---

**Happy Airdrop Hunting! 🚀**
