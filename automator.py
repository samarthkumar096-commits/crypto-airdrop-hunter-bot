"""
Browser Automation Module
Automates social tasks and form filling for airdrops
IMPORTANT: Does NOT handle wallet transactions - you approve manually!
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class AirdropAutomator:
    def __init__(self, config):
        self.config = config
        self.driver = None
        
    def setup_browser(self, headless=False):
        """Initialize Chrome browser"""
        chrome_options = Options()
        
        if headless:
            chrome_options.add_argument('--headless')
        
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # User agent
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        print("✅ Browser initialized")
        
    def close_browser(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()
            print("✅ Browser closed")
    
    def automate_trex(self):
        """Automate T-Rex daily tasks"""
        print("\n🤖 Automating T-Rex tasks...")
        
        try:
            self.driver.get('https://trex.xyz')
            time.sleep(3)
            
            # Wait for page load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            print("✅ T-Rex page loaded")
            print("⚠️  MANUAL ACTION REQUIRED:")
            print("   1. Connect your wallet")
            print("   2. Complete daily quests")
            print("   3. Claim badges")
            
            # Keep browser open for manual actions
            input("\nPress Enter when done...")
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def automate_prismax(self):
        """Automate PrismaX daily login"""
        print("\n🤖 Automating PrismaX tasks...")
        
        try:
            self.driver.get('https://app.prismax.ai')
            time.sleep(3)
            
            print("✅ PrismaX app loaded")
            print("⚠️  MANUAL ACTION REQUIRED:")
            print("   1. Connect Phantom wallet")
            print("   2. Daily login (automatic +10 points)")
            print("   3. Complete profile if needed")
            
            input("\nPress Enter when done...")
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def auto_fill_form(self, form_data):
        """Auto-fill common airdrop forms"""
        try:
            # Find wallet address field
            wallet_fields = self.driver.find_elements(By.XPATH, 
                "//input[contains(@placeholder, 'wallet') or contains(@name, 'address')]")
            
            if wallet_fields and self.config.get('wallet_address'):
                wallet_fields[0].send_keys(self.config['wallet_address'])
                print("✅ Wallet address filled")
            
            # Find email field
            email_fields = self.driver.find_elements(By.XPATH,
                "//input[@type='email' or contains(@name, 'email')]")
            
            if email_fields and self.config.get('email'):
                email_fields[0].send_keys(self.config['email'])
                print("✅ Email filled")
            
            # Find Twitter field
            twitter_fields = self.driver.find_elements(By.XPATH,
                "//input[contains(@placeholder, 'twitter') or contains(@name, 'twitter')]")
            
            if twitter_fields and self.config.get('twitter_username'):
                twitter_fields[0].send_keys(self.config['twitter_username'])
                print("✅ Twitter username filled")
            
            return True
            
        except Exception as e:
            print(f"❌ Form fill error: {e}")
            return False
    
    def complete_social_tasks(self, tasks):
        """Open social task links in new tabs"""
        print("\n📱 Opening social tasks...")
        
        for task in tasks:
            if 'twitter' in task.lower():
                print(f"🐦 Twitter task: {task}")
                # Open in new tab
                self.driver.execute_script("window.open('https://twitter.com');")
                
            elif 'discord' in task.lower():
                print(f"💬 Discord task: {task}")
                self.driver.execute_script("window.open('https://discord.com');")
                
            elif 'telegram' in task.lower():
                print(f"✈️ Telegram task: {task}")
                self.driver.execute_script("window.open('https://t.me');")
        
        print("\n⚠️  Complete tasks manually in opened tabs")
        input("Press Enter when all tasks completed...")
    
    def run_daily_routine(self):
        """Run daily airdrop tasks"""
        print("\n🚀 Starting Daily Airdrop Routine\n")
        
        self.setup_browser(headless=False)
        
        try:
            # T-Rex
            print("=" * 50)
            self.automate_trex()
            time.sleep(2)
            
            # PrismaX
            print("=" * 50)
            self.automate_prismax()
            time.sleep(2)
            
            print("\n✅ Daily routine completed!")
            
        except Exception as e:
            print(f"❌ Error in routine: {e}")
            
        finally:
            input("\nPress Enter to close browser...")
            self.close_browser()

if __name__ == "__main__":
    # Test automation
    config = {
        'wallet_address': '0xYourWalletAddress',
        'email': 'your@email.com',
        'twitter_username': '@yourusername'
    }
    
    automator = AirdropAutomator(config)
    automator.run_daily_routine()
