"""
Scheduler Module - Run bot on schedule
"""

import schedule
import time
from datetime import datetime
from airdrop_hunter import AirdropHunter

def daily_scan():
    """Daily airdrop scan job"""
    print(f"\n⏰ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running scheduled scan...")
    
    hunter = AirdropHunter()
    hunter.scan_airdrops()
    
    print("✅ Scheduled scan completed\n")

def daily_reminder():
    """Daily task reminder"""
    print(f"\n🔔 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Daily Task Reminder!")
    print("\n📋 Don't forget your daily tasks:")
    print("   • PrismaX: Daily login → app.prismax.ai")
    print("   • T-Rex: Check quests → trex.xyz")
    print("   • Hotstuff: Testnet activity")
    print("\n⏱️  Takes only 10 minutes!\n")

def weekly_report():
    """Weekly summary report"""
    print(f"\n📊 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Weekly Report")
    print("\n" + "="*50)
    print("WEEKLY AIRDROP SUMMARY")
    print("="*50)
    
    hunter = AirdropHunter()
    hunter.view_current_airdrops()
    hunter.check_values()
    
    print("✅ Weekly report completed\n")

def main():
    """Main scheduler"""
    print("🤖 Airdrop Hunter Scheduler Started")
    print("="*50)
    
    # Schedule jobs
    schedule.every().day.at("09:00").do(daily_scan)
    schedule.every().day.at("10:30").do(daily_reminder)
    schedule.every().sunday.at("20:00").do(weekly_report)
    
    print("📅 Scheduled Jobs:")
    print("   • Daily Scan: 9:00 AM")
    print("   • Daily Reminder: 10:30 AM")
    print("   • Weekly Report: Sunday 8:00 PM")
    print("\n⏳ Scheduler running... (Press Ctrl+C to stop)\n")
    
    # Run scheduler
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
            
    except KeyboardInterrupt:
        print("\n\n👋 Scheduler stopped")

if __name__ == "__main__":
    main()
