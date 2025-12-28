"""
Crypto Airdrop Hunter Bot - Main Scanner Module
Automatically discovers and tracks FREE crypto airdrops
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

class AirdropScanner:
    def __init__(self, config):
        self.config = config
        self.airdrops = []
        
    def scan_cryptorank(self):
        """Scan CryptoRank for latest airdrops"""
        print("🔍 Scanning CryptoRank...")
        
        try:
            # CryptoRank API endpoint (public data)
            url = "https://cryptorank.io/drophunting"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Parse airdrop data (simplified - actual parsing depends on site structure)
                airdrops_found = []
                
                # Example structure - adjust based on actual HTML
                airdrop_cards = soup.find_all('div', class_='airdrop-card')
                
                for card in airdrop_cards[:10]:  # Top 10
                    try:
                        name = card.find('h3').text.strip()
                        status = card.find('span', class_='status').text.strip()
                        value = card.find('span', class_='value').text.strip()
                        
                        # Only FREE airdrops
                        if 'free' in value.lower() or '$0' in value:
                            airdrops_found.append({
                                'name': name,
                                'status': status,
                                'value': value,
                                'source': 'CryptoRank',
                                'timestamp': datetime.now().isoformat()
                            })
                    except:
                        continue
                
                print(f"✅ Found {len(airdrops_found)} FREE airdrops on CryptoRank")
                return airdrops_found
                
        except Exception as e:
            print(f"❌ Error scanning CryptoRank: {e}")
            return []
    
    def scan_airdrops_io(self):
        """Scan Airdrops.io for latest opportunities"""
        print("🔍 Scanning Airdrops.io...")
        
        try:
            url = "https://airdrops.io"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                airdrops_found = []
                
                # Parse active airdrops
                airdrop_items = soup.find_all('div', class_='airdrop-item')
                
                for item in airdrop_items[:10]:
                    try:
                        name = item.find('h4').text.strip()
                        link = item.find('a')['href']
                        
                        airdrops_found.append({
                            'name': name,
                            'link': link,
                            'source': 'Airdrops.io',
                            'timestamp': datetime.now().isoformat()
                        })
                    except:
                        continue
                
                print(f"✅ Found {len(airdrops_found)} airdrops on Airdrops.io")
                return airdrops_found
                
        except Exception as e:
            print(f"❌ Error scanning Airdrops.io: {e}")
            return []
    
    def check_legitimacy(self, airdrop):
        """Basic scam detection"""
        red_flags = [
            'send eth', 'send bnb', 'private key', 'seed phrase',
            'double your', 'guaranteed', 'elon musk', 'giveaway'
        ]
        
        name_lower = airdrop.get('name', '').lower()
        
        for flag in red_flags:
            if flag in name_lower:
                return False
        
        return True
    
    def scan_all(self):
        """Run all scanners"""
        print("\n🚀 Starting Airdrop Hunt...\n")
        
        all_airdrops = []
        
        # Scan multiple sources
        all_airdrops.extend(self.scan_cryptorank())
        time.sleep(2)  # Rate limiting
        
        all_airdrops.extend(self.scan_airdrops_io())
        
        # Filter legitimate only
        legitimate = [a for a in all_airdrops if self.check_legitimacy(a)]
        
        # Remove duplicates
        unique_airdrops = []
        seen_names = set()
        
        for airdrop in legitimate:
            name = airdrop.get('name', '')
            if name not in seen_names:
                unique_airdrops.append(airdrop)
                seen_names.add(name)
        
        self.airdrops = unique_airdrops
        
        print(f"\n✅ Total legitimate airdrops found: {len(unique_airdrops)}\n")
        
        return unique_airdrops
    
    def get_current_airdrops(self):
        """Get manually curated current airdrops"""
        return [
            {
                'name': 'T-Rex',
                'website': 'https://trex.xyz',
                'value': '1170 points',
                'time': '33 minutes',
                'tasks': ['Sign up', 'Connect wallet', 'Complete badges', 'Daily quests'],
                'status': 'Confirmed',
                'cost': 'FREE'
            },
            {
                'name': 'PrismaX',
                'website': 'https://app.prismax.ai',
                'value': '1782 points',
                'time': '11 minutes',
                'tasks': ['Connect Phantom wallet', 'Complete profile', 'Daily login'],
                'status': 'Potential',
                'cost': 'FREE'
            },
            {
                'name': 'Hotstuff',
                'website': 'Check @tradehotstuff on Twitter',
                'value': '1265 points',
                'time': '10 minutes',
                'tasks': ['Join waitlist', 'Testnet participation', 'Social tasks'],
                'status': 'Potential',
                'cost': 'FREE'
            }
        ]
    
    def save_results(self, filename='airdrops.json'):
        """Save scan results to file"""
        data = {
            'scan_time': datetime.now().isoformat(),
            'total_found': len(self.airdrops),
            'airdrops': self.airdrops
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Results saved to {filename}")

if __name__ == "__main__":
    # Test scanner
    config = {}
    scanner = AirdropScanner(config)
    
    # Get current known airdrops
    current = scanner.get_current_airdrops()
    
    print("📋 Current Active FREE Airdrops:\n")
    for airdrop in current:
        print(f"✅ {airdrop['name']}")
        print(f"   Website: {airdrop['website']}")
        print(f"   Value: {airdrop['value']}")
        print(f"   Time: {airdrop['time']}")
        print(f"   Status: {airdrop['status']}")
        print()
    
    # Scan for new ones
    # scanner.scan_all()
    # scanner.save_results()
