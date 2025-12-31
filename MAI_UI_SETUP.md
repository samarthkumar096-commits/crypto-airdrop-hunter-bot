# MAI-UI Setup and Deployment Guide

## 🤖 What is MAI-UI?

MAI-UI is an AI agent that can control your phone/computer screen automatically - like a virtual assistant that can actually use apps!

**Created by:** Alibaba's Tongyi-MAI team
**Released:** December 29, 2025
**Performance:** State-of-the-art (beats Gemini-3-Pro!)

---

## 🎯 Integration with Your Telegram Bot

Your bot now has **MAI-UI integration** that allows users to automate GUI tasks!

### **New Command:**
```
/automate <task>
```

### **Example Usage:**
```
/automate Book train from Beijing to Shanghai tomorrow
/automate Search iPhone 15 on Taobao and add to cart
/automate Send message to Work Group on WeChat
```

---

## 🚀 Setup MAI-UI (Optional)

If you want to enable GUI automation, follow these steps:

### **Step 1: Requirements**

**Hardware:**
- GPU with 8GB+ VRAM (for MAI-UI-8B)
- Or 2GB+ VRAM (for MAI-UI-2B)
- 16GB+ RAM
- 50GB+ disk space

**Software:**
- Python 3.8+
- CUDA 11.8+ (for GPU)
- vLLM

### **Step 2: Install MAI-UI**

```bash
# Clone MAI-UI repository
git clone https://github.com/Tongyi-MAI/MAI-UI.git
cd MAI-UI

# Install dependencies
pip install -r requirements.txt

# Install vLLM
pip install vllm  # vllm>=0.11.0
```

### **Step 3: Download Model**

**Choose model based on your hardware:**

**Option A: MAI-UI-2B (Lightweight)**
```bash
# Download from HuggingFace
huggingface-cli download Tongyi-MAI/MAI-UI-2B
```

**Option B: MAI-UI-8B (Recommended)**
```bash
# Download from HuggingFace
huggingface-cli download Tongyi-MAI/MAI-UI-8B
```

**Models:**
- MAI-UI-2B: ~4GB (on-device, phone)
- MAI-UI-8B: ~16GB (small server)
- MAI-UI-32B: ~64GB (powerful server)

### **Step 4: Start MAI-UI Server**

```bash
# Start vLLM API server
python -m vllm.entrypoints.openai.api_server \
    --model Tongyi-MAI/MAI-UI-8B \
    --served-model-name MAI-UI-8B \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 1 \
    --trust-remote-code
```

**Server will run at:** `http://localhost:8000/v1`

### **Step 5: Configure Your Bot**

Update `mai_ui_integration.py`:

```python
mai_ui = MAIUIIntegration(
    api_base_url="http://YOUR_SERVER_IP:8000/v1",  # Update this
    model_name="MAI-UI-8B"
)
```

### **Step 6: Test Integration**

```bash
# Test MAI-UI server
curl http://localhost:8000/v1/models

# Should return: {"data": [{"id": "MAI-UI-8B", ...}]}
```

---

## 💡 Usage Examples

### **Example 1: Shopping**
```
User: /automate Search wireless headphones on Taobao under 200 yuan, add top rated to cart

Bot: 
✅ Task Completed!
- Opened Taobao
- Searched "wireless headphones"
- Filtered price < 200 yuan
- Sorted by rating
- Added top item to cart
```

### **Example 2: Booking**
```
User: /automate Book train Beijing to Shanghai tomorrow morning

Bot:
✅ Task Completed!
- Opened 12306 app
- Searched Beijing → Shanghai
- Date: Tomorrow
- Time: Morning
- Showing available tickets
```

### **Example 3: Messaging**
```
User: /automate Send "Meeting at 3 PM" to Work Group on WeChat

Bot:
✅ Task Completed!
- Opened WeChat
- Found "Work Group"
- Sent message: "Meeting at 3 PM"
```

### **Example 4: Multi-app**
```
User: /automate Search iPhone 15 on Xiaohongshu, save image, search on Taobao

Bot:
✅ Task Completed!
- Opened Xiaohongshu
- Searched "iPhone 15"
- Saved top image
- Opened Taobao
- Image search
- Showing results
```

---

## 🔧 Troubleshooting

### **MAI-UI Not Available**

If you see "MAI-UI Service Not Available":

1. **Check if server is running:**
   ```bash
   curl http://localhost:8000/v1/models
   ```

2. **Check logs:**
   ```bash
   # Check vLLM logs for errors
   ```

3. **Verify GPU:**
   ```bash
   nvidia-smi  # Should show GPU usage
   ```

### **Out of Memory**

If you get OOM errors:

1. **Use smaller model:**
   - Switch from MAI-UI-8B to MAI-UI-2B

2. **Reduce batch size:**
   ```bash
   --max-num-seqs 1
   ```

3. **Use CPU (slower):**
   ```bash
   # Remove --tensor-parallel-size flag
   ```

---

## 📊 Performance

### **MAI-UI Benchmarks:**

| Benchmark | Score | Rank |
|-----------|-------|------|
| ScreenSpot-Pro | 73.5% | #1 |
| MMBench GUI | 91.3% | #1 |
| AndroidWorld | 76.7% | #1 |
| MobileWorld | 41.7% | Top 3 |

**Beats:** Gemini-3-Pro, Seed1.8, UI-Tars-2

---

## 🎁 What You Get

### **With MAI-UI Integration:**

✅ **GUI Automation** - Control apps automatically
✅ **Multi-app Workflows** - Complex cross-app tasks
✅ **Natural Language** - Just describe what you want
✅ **Screen Understanding** - AI sees and understands UI
✅ **Smart Actions** - Clicks, types, scrolls automatically
✅ **User Interaction** - Asks questions when needed

### **Without MAI-UI:**

Your bot still works perfectly for:
- ✅ Airdrop hunting
- ✅ HotStuff tracking
- ✅ Crypto monitoring
- ✅ Notifications

MAI-UI is **optional** - adds GUI automation on top!

---

## 🔗 Resources

**MAI-UI GitHub:**
```
https://github.com/Tongyi-MAI/MAI-UI
```

**Paper:**
```
https://arxiv.org/abs/2512.22047
```

**Models:**
```
https://huggingface.co/Tongyi-MAI/MAI-UI-2B
https://huggingface.co/Tongyi-MAI/MAI-UI-8B
```

**Website:**
```
https://tongyi-mai.github.io/MAI-UI/
```

---

## 💰 Cost

### **Free Options:**

**1. Run Locally (FREE)**
- Use your own GPU
- No API costs
- Full control

**2. Cloud GPU (Paid)**
- Rent GPU server
- ~$0.50-2/hour
- On-demand

### **Recommended Setup:**

**For Testing:**
- Use MAI-UI-2B locally
- FREE

**For Production:**
- Rent GPU server
- Deploy MAI-UI-8B
- ~$50-100/month

---

## 🎯 Summary

**MAI-UI Integration:**
- ✅ Added to your bot
- ✅ `/automate` command ready
- ⏳ Needs MAI-UI server (optional)

**Your Bot Works:**
- ✅ Without MAI-UI (airdrop hunting)
- ✅ With MAI-UI (+ GUI automation)

**Setup MAI-UI:**
- Optional but powerful!
- Adds screen control
- Natural language automation

---

**Your bot is ready! MAI-UI integration is there, just needs server setup if you want GUI automation!** 🚀
