"""
EASY SETUP SCRIPT
Run this once to configure everything automatically
"""

import json
import os

def easy_setup():
    """Interactive setup wizard"""
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🚀 CRYPTO AIRDROP HUNTER - EASY SETUP 🚀             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

Welcome! Let's set up your airdrop hunter in 2 minutes.

⚠️  IMPORTANT: You'll connect wallet when using the bot.
    This setup just configures basic info.
    """)
    
    print("\n" + "="*60)
    print("STEP 1: Basic Information")
    print("="*60)
    
    # Get wallet address
    wallet = input("\n📍 Your wallet address (for form auto-fill): ").strip()
    if not wallet:
        wallet = "0x0000000000000000000000000000000000000000"
        print("   ⚠️  Skipped - you can add later")
    
    # Get email
    email = input("\n📧 Your email (for notifications): ").strip()
    if not email:
        email = "your@email.com"
        print("   ⚠️  Skipped - you can add later")
    
    # Get Twitter
    twitter = input("\n🐦 Your Twitter username (e.g., @username): ").strip()
    if not twitter:
        twitter = "@yourusername"
        print("   ⚠️  Skipped - you can add later")
    
    print("\n" + "="*60)
    print("STEP 2: Automation Preferences")
    print("="*60)
    
    # Auto-open browser
    auto_browser = input("\n🌐 Auto-open claim pages daily? (y/n): ").strip().lower()
    auto_browser = auto_browser == 'y'
    
    # Notification preference
    notifications = input("\n🔔 Enable daily reminders? (y/n): ").strip().lower()
    notifications = notifications == 'y'
    
    # Create config
    config = {
        "wallet_address": wallet,
        "email": email,
        "twitter_username": twitter,
        "discord_username": "",
        "telegram_bot_token": "",
        "telegram_chat_id": "",
        "scan_interval_hours": 24,
        "auto_claim": False,  # Always false for safety
        "auto_open_browser": auto_browser,
        "telegram_notifications": False,
        "daily_reminders": notifications,
        "notification_settings": {
            "new_airdrops": True,
            "daily_tasks": notifications,
            "value_updates": False
        },
        "filter_settings": {
            "min_estimated_value": 0,
            "only_confirmed": False,
            "exclude_testnets": False,
            "preferred_chains": ["Ethereum", "Arbitrum", "Solana", "Base"]
        }
    }
    
    # Save config
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n" + "="*60)
    print("✅ SETUP COMPLETE!")
    print("="*60)
    
    print(f"""
📋 Your Configuration:
   Wallet: {wallet[:10]}...
   Email: {email}
   Twitter: {twitter}
   Auto-browser: {'Yes' if auto_browser else 'No'}
   Reminders: {'Yes' if notifications else 'No'}

💾 Saved to: config.json

🚀 NEXT STEPS:
   1. Run: python airdrop_hunter.py
   2. Select option 3 (Run Automation)
   3. Connect your wallet when prompted
   4. Bot will handle the rest!

⏰ DAILY ROUTINE:
   - Bot finds airdrops (automated)
   - Bot opens pages (automated)
   - You click "Claim" (5 seconds)
   - Profit! 💰

🔒 SECURITY:
   ✅ Private keys NEVER stored
   ✅ You control all transactions
   ✅ Bot only helps with tasks

═══════════════════════════════════════════════════════════

Ready to start? Run: python airdrop_hunter.py
    """)

if __name__ == "__main__":
    try:
        easy_setup()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please try again or edit config.json manually")
