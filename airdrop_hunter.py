"""
Main Airdrop Hunter Bot
Combines scanning, automation, and notifications
"""

import json
import time
from datetime import datetime
from scanner import AirdropScanner
from automator import AirdropAutomator

class AirdropHunter:
    def __init__(self, config_file='config.json'):
        self.config = self.load_config(config_file)
        self.scanner = AirdropScanner(self.config)
        self.automator = AirdropAutomator(self.config)
        
    def load_config(self, config_file):
        """Load configuration"""
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            print("✅ Configuration loaded")
            return config
        except FileNotFoundError:
            print("⚠️  Config file not found, using defaults")
            return self.get_default_config()
    
    def get_default_config(self):
        """Default configuration"""
        return {
            'wallet_address': '',
            'email': '',
            'twitter_username': '',
            'discord_username': '',
            'scan_interval_hours': 24,
            'auto_claim': False,
            'telegram_notifications': False
        }
    
    def display_banner(self):
        """Display bot banner"""
        banner = """
╔═══════════════════════════════════════════════════╗
║                                                   ║
║        🚀 CRYPTO AIRDROP HUNTER BOT 🚀           ║
║                                                   ║
║     Automated FREE Crypto Airdrop Discovery      ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
        """
        print(banner)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. 🔍 Scan for New Airdrops")
        print("2. 📋 View Current Active Airdrops")
        print("3. 🤖 Run Daily Task Automation")
        print("4. 💰 Check Airdrop Value Estimates")
        print("5. ⚙️  Configure Settings")
        print("6. 📊 View Statistics")
        print("7. ❌ Exit")
        print("="*50)
    
    def scan_airdrops(self):
        """Scan for new airdrops"""
        print("\n🔍 Scanning for airdrops...\n")
        airdrops = self.scanner.scan_all()
        
        if airdrops:
            print("\n📋 Found Airdrops:\n")
            for i, airdrop in enumerate(airdrops, 1):
                print(f"{i}. {airdrop.get('name', 'Unknown')}")
                print(f"   Source: {airdrop.get('source', 'N/A')}")
                print(f"   Status: {airdrop.get('status', 'N/A')}")
                print()
        else:
            print("❌ No new airdrops found")
    
    def view_current_airdrops(self):
        """View current active airdrops"""
        print("\n📋 CURRENT ACTIVE FREE AIRDROPS\n")
        print("="*70)
        
        airdrops = self.scanner.get_current_airdrops()
        
        for i, airdrop in enumerate(airdrops, 1):
            print(f"\n{i}. {airdrop['name']} ({airdrop['status']})")
            print(f"   🌐 Website: {airdrop['website']}")
            print(f"   💰 Value: {airdrop['value']}")
            print(f"   ⏱️  Time: {airdrop['time']}")
            print(f"   💵 Cost: {airdrop['cost']}")
            print(f"   📝 Tasks:")
            for task in airdrop['tasks']:
                print(f"      • {task}")
        
        print("\n" + "="*70)
    
    def run_automation(self):
        """Run daily task automation"""
        print("\n🤖 Starting Automation...\n")
        
        if not self.config.get('wallet_address'):
            print("⚠️  Warning: Wallet address not configured!")
            print("   Some features may not work properly.")
            print("   Edit config.json to add your details.\n")
        
        confirm = input("Continue with automation? (y/n): ")
        
        if confirm.lower() == 'y':
            self.automator.run_daily_routine()
        else:
            print("❌ Automation cancelled")
    
    def check_values(self):
        """Display value estimates"""
        print("\n💰 AIRDROP VALUE ESTIMATES\n")
        print("="*70)
        print("\nBased on similar past airdrops:\n")
        
        estimates = [
            {
                'name': 'T-Rex (1170 points)',
                'conservative': '$10-50',
                'realistic': '$50-200',
                'optimistic': '$200-500'
            },
            {
                'name': 'PrismaX (1782 points)',
                'conservative': '$15-75',
                'realistic': '$75-300',
                'optimistic': '$300-750'
            },
            {
                'name': 'Hotstuff (1265 points)',
                'conservative': '$10-60',
                'realistic': '$60-250',
                'optimistic': '$250-600'
            }
        ]
        
        for est in estimates:
            print(f"📊 {est['name']}")
            print(f"   Conservative: {est['conservative']}")
            print(f"   Realistic: {est['realistic']}")
            print(f"   Optimistic: {est['optimistic']}")
            print()
        
        print("⚠️  DISCLAIMER: These are estimates only!")
        print("   Actual values may be $0 or much higher.")
        print("   Past performance ≠ future results.\n")
        print("="*70)
    
    def configure_settings(self):
        """Configure bot settings"""
        print("\n⚙️  CONFIGURATION\n")
        print("="*50)
        print(f"Current wallet: {self.config.get('wallet_address', 'Not set')}")
        print(f"Email: {self.config.get('email', 'Not set')}")
        print(f"Twitter: {self.config.get('twitter_username', 'Not set')}")
        print("="*50)
        print("\nEdit config.json file to update settings")
        print("Then restart the bot.\n")
    
    def view_stats(self):
        """View bot statistics"""
        print("\n📊 STATISTICS\n")
        print("="*50)
        print("Total Airdrops Tracked: 3")
        print("Estimated Total Value: $30-1500")
        print("Time Investment: ~54 minutes (one-time)")
        print("Daily Maintenance: ~10 minutes")
        print("="*50)
    
    def run(self):
        """Main bot loop"""
        self.display_banner()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nSelect option (1-7): ").strip()
                
                if choice == '1':
                    self.scan_airdrops()
                elif choice == '2':
                    self.view_current_airdrops()
                elif choice == '3':
                    self.run_automation()
                elif choice == '4':
                    self.check_values()
                elif choice == '5':
                    self.configure_settings()
                elif choice == '6':
                    self.view_stats()
                elif choice == '7':
                    print("\n👋 Thanks for using Airdrop Hunter!")
                    print("🚀 Happy airdrop hunting!\n")
                    break
                else:
                    print("❌ Invalid option. Please select 1-7.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting...")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    hunter = AirdropHunter()
    hunter.run()
