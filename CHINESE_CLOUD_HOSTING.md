# 🇨🇳 Chinese Cloud Hosting for Telegram Bot

## 🏆 Top 3 Chinese Cloud Platforms (2025)

---

## 1️⃣ Alibaba Cloud (阿里云) - ⭐ BEST!

### **Why #1:**
- ✅ **Largest Chinese cloud** provider
- ✅ **AI-powered** (Qwen models)
- ✅ **Free tier** available
- ✅ **Global reach** (170+ countries)
- ✅ **Python optimized**
- ✅ **Cost-effective** (5-200x cheaper than AWS)
- ✅ **Excellent for bots**

### **Free Tier:**
- 🎁 **ECS (Elastic Compute):** 1 month free trial
- 🎁 **Function Compute:** 1M invocations/month free
- 🎁 **Container Service:** Free tier available
- 🎁 **API Credits:** For AI models

### **Deploy Your Bot:**

#### **Method 1: ECS (Virtual Machine)**

**Step 1:** Sign up
```
https://www.alibabacloud.com
```

**Step 2:** Create ECS Instance
- Region: Hong Kong / Singapore (for international)
- OS: Ubuntu 22.04
- Instance Type: ecs.t5-lc1m1.small (free tier)
- Storage: 20GB

**Step 3:** Connect via SSH
```bash
ssh root@your-instance-ip
```

**Step 4:** Setup Bot
```bash
# Update system
apt update && apt upgrade -y

# Install Python
apt install python3 python3-pip git -y

# Clone your bot
git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git
cd crypto-airdrop-hunter-bot

# Install dependencies
pip3 install -r requirements.txt

# Create config
cat > config.json << EOF
{
  "telegram_bot_token": "8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY",
  "telegram_chat_id": "5428245719"
}
EOF

# Run bot in background
nohup python3 telegram_bot.py > bot.log 2>&1 &
```

**Step 5:** Keep Bot Running (systemd)
```bash
# Create service file
cat > /etc/systemd/system/telegram-bot.service << EOF
[Unit]
Description=Telegram Airdrop Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/crypto-airdrop-hunter-bot
ExecStart=/usr/bin/python3 telegram_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable and start
systemctl enable telegram-bot
systemctl start telegram-bot
systemctl status telegram-bot
```

**DONE!** Bot running 24/7! 🎉

#### **Method 2: Function Compute (Serverless)**

**Step 1:** Create Function
- Runtime: Python 3.9
- Trigger: Timer (every 5 minutes)

**Step 2:** Upload Code
```bash
zip -r bot.zip telegram_bot.py requirements.txt config.json
```

**Step 3:** Configure
- Memory: 512 MB
- Timeout: 300 seconds
- Environment Variables:
  - `TELEGRAM_BOT_TOKEN`
  - `TELEGRAM_CHAT_ID`

**Step 4:** Deploy & Test

---

## 2️⃣ Tencent Cloud (腾讯云) - Great Alternative!

### **Why Good:**
- ✅ **WeChat integration**
- ✅ **Strong in China**
- ✅ **Serverless options**
- ✅ **Free trial credits**
- ✅ **Good for social bots**

### **Free Tier:**
- 🎁 **CVM (Cloud Virtual Machine):** 3 months free
- 🎁 **SCF (Serverless):** 1M invocations/month
- 🎁 **TKE (Kubernetes):** Free tier

### **Deploy:**

**Step 1:** Sign up
```
https://intl.cloud.tencent.com
```

**Step 2:** Create CVM Instance
- Region: Hong Kong / Singapore
- OS: Ubuntu 20.04
- Instance: 1 Core, 1GB RAM (free tier)

**Step 3:** Setup (same as Alibaba Cloud ECS method)

---

## 3️⃣ Huawei Cloud (华为云) - Enterprise Grade!

### **Why Good:**
- ✅ **18% market share**
- ✅ **Global presence**
- ✅ **AI frameworks**
- ✅ **Enterprise features**
- ✅ **Free trial**

### **Free Tier:**
- 🎁 **ECS:** Free trial credits
- 🎁 **FunctionGraph:** Serverless free tier
- 🎁 **CCE (Kubernetes):** Free tier

### **Deploy:**

**Step 1:** Sign up
```
https://www.huaweicloud.com/intl/en-us/
```

**Step 2:** Create ECS
- Region: Hong Kong / Singapore
- OS: Ubuntu
- Flavor: s6.small.1 (1 vCPU, 1GB)

**Step 3:** Setup (same as above)

---

## 📊 Comparison Table

| Platform | Free Tier | Setup Time | Best For | Cost After Free |
|----------|-----------|------------|----------|-----------------|
| **Alibaba Cloud** | 1 month + credits | 10 min | AI bots, general | $5-10/month |
| **Tencent Cloud** | 3 months | 10 min | Social bots | $5-8/month |
| **Huawei Cloud** | Trial credits | 10 min | Enterprise | $8-12/month |

---

## 🎯 Recommendation

### **Use Alibaba Cloud**

**Why?**
1. ✅ **Best free tier**
2. ✅ **AI-optimized** (Qwen models)
3. ✅ **Most cost-effective**
4. ✅ **Largest ecosystem**
5. ✅ **Best documentation**
6. ✅ **Global reach**

---

## 🚀 Quick Start (Alibaba Cloud)

### **Fastest Method:**

**Step 1:** Sign up at https://www.alibabacloud.com

**Step 2:** Activate free tier

**Step 3:** Create ECS instance (Ubuntu)

**Step 4:** Run setup script:
```bash
curl -fsSL https://raw.githubusercontent.com/samarthkumar096-commits/crypto-airdrop-hunter-bot/main/setup.sh | bash
```

**Step 5:** Add your tokens:
```bash
export TELEGRAM_BOT_TOKEN="8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY"
export TELEGRAM_CHAT_ID="5428245719"
```

**Step 6:** Start bot:
```bash
systemctl start telegram-bot
```

**DONE!** Bot live 24/7! 🎉

---

## 💡 Pro Tips

### **1. Choose Right Region:**
- **For China users:** Beijing, Shanghai, Shenzhen
- **For International:** Hong Kong, Singapore, Tokyo
- **Best latency:** Hong Kong (global access)

### **2. Security:**
```bash
# Setup firewall
ufw allow 22/tcp
ufw allow 443/tcp
ufw enable

# Update regularly
apt update && apt upgrade -y
```

### **3. Monitoring:**
```bash
# Check bot status
systemctl status telegram-bot

# View logs
journalctl -u telegram-bot -f

# Check resource usage
htop
```

### **4. Auto-restart on failure:**
```bash
# Already configured in systemd service
# Bot will auto-restart if it crashes
```

---

## 🔧 Troubleshooting

### **Bot not starting?**

**Check logs:**
```bash
journalctl -u telegram-bot -n 50
```

**Common issues:**
1. ❌ Wrong token → Check config.json
2. ❌ Dependencies missing → Run `pip3 install -r requirements.txt`
3. ❌ Port blocked → Check firewall

### **Connection issues?**

**Test connectivity:**
```bash
# Test Telegram API
curl https://api.telegram.org/bot8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY/getMe

# Check DNS
ping api.telegram.org
```

---

## 💰 Cost Comparison

### **After Free Tier:**

| Platform | Monthly Cost | Specs |
|----------|-------------|-------|
| **Alibaba Cloud** | $5-10 | 1 vCPU, 1GB RAM |
| **Tencent Cloud** | $5-8 | 1 vCPU, 1GB RAM |
| **Huawei Cloud** | $8-12 | 1 vCPU, 1GB RAM |

**All cheaper than Western clouds!** 💰

---

## 🌏 Regional Considerations

### **For International Users:**

✅ **Use Hong Kong/Singapore regions**
- No ICP license needed
- Better international connectivity
- English support available

### **For China Users:**

✅ **Use mainland regions**
- Better latency
- ICP license required for production
- Chinese support

---

## 🎁 Bonus: Docker Deployment

### **Even Easier with Docker:**

**Step 1:** Install Docker
```bash
curl -fsSL https://get.docker.com | sh
```

**Step 2:** Run bot
```bash
docker run -d \
  --name telegram-bot \
  --restart always \
  -e TELEGRAM_BOT_TOKEN="8482827002:AAGIFEBwpQlOYwxuKebcTPQKAl-y2ZbGJZY" \
  -e TELEGRAM_CHAT_ID="5428245719" \
  python:3.11 \
  bash -c "git clone https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot.git && cd crypto-airdrop-hunter-bot && pip install -r requirements.txt && python telegram_bot.py"
```

**DONE!** One command deployment! 🚀

---

## ✅ Verification

**After deployment:**

1. Open Telegram
2. Go to @samarth_airdrop_hunter_bot
3. Send `/start`
4. Bot replies = SUCCESS! ✅

---

## 📱 Quick Links

- **Alibaba Cloud:** https://www.alibabacloud.com
- **Tencent Cloud:** https://intl.cloud.tencent.com
- **Huawei Cloud:** https://www.huaweicloud.com/intl/en-us/
- **Your Bot:** @samarth_airdrop_hunter_bot
- **GitHub:** https://github.com/samarthkumar096-commits/crypto-airdrop-hunter-bot

---

## 🎯 Summary

**Best Choice:** Alibaba Cloud
**Setup Time:** 10 minutes
**Cost:** FREE (1 month) → $5-10/month
**Uptime:** 99.9%
**Difficulty:** Medium (but worth it!)

**Perfect for serious bot hosting!** 🚀

---

**Deploy on Alibaba Cloud and start earning!** 💰
