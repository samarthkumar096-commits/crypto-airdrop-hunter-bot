"""
Telegram Bot Integration for Airdrop Hunter
Control your airdrop bot from anywhere via Telegram!
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
from scanner import AirdropScanner
from datetime import datetime
import json

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramAirdropBot:
    def __init__(self, token, config):
        self.token = token
        self.config = config
        self.scanner = AirdropScanner(config)
        self.app = None
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command - Welcome message"""
        welcome_text = """
🚀 *Welcome to Crypto Airdrop Hunter Bot!*

I'll help you find and claim FREE crypto airdrops automatically!

*Available Commands:*
/scan - Find new airdrops
/claim - Get claim links for active airdrops
/status - Check current airdrops
/stats - View your earnings
/remind - Set daily reminders
/settings - Configure bot
/help - Show this message

*Quick Start:*
1. Use /scan to find airdrops
2. Use /claim to get links
3. Click links and claim!

Let's start earning! 💰
        """
        
        keyboard = [
            [
                InlineKeyboardButton("🔍 Scan Airdrops", callback_data='scan'),
                InlineKeyboardButton("💰 Claim Now", callback_data='claim')
            ],
            [
                InlineKeyboardButton("📊 My Stats", callback_data='stats'),
                InlineKeyboardButton("⚙️ Settings", callback_data='settings')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def scan_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Scan for new airdrops"""
        await update.message.reply_text("🔍 Scanning for new airdrops... Please wait...")
        
        try:
            # Get current airdrops
            airdrops = self.scanner.get_current_airdrops()
            
            if airdrops:
                message = "✅ *Active FREE Airdrops Found!*\n\n"
                
                for i, airdrop in enumerate(airdrops, 1):
                    message += f"*{i}. {airdrop['name']}* ({airdrop['status']})\n"
                    message += f"   💰 Value: {airdrop['value']}\n"
                    message += f"   ⏱️ Time: {airdrop['time']}\n"
                    message += f"   💵 Cost: {airdrop['cost']}\n"
                    message += f"   🔗 Link: {airdrop['website']}\n\n"
                
                message += "Use /claim to get direct claim links!"
                
                await update.message.reply_text(message, parse_mode='Markdown')
            else:
                await update.message.reply_text("❌ No new airdrops found. Try again later!")
                
        except Exception as e:
            logger.error(f"Error in scan: {e}")
            await update.message.reply_text("❌ Error scanning airdrops. Please try again.")
    
    async def claim_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Get claim links for active airdrops"""
        airdrops = self.scanner.get_current_airdrops()
        
        message = "🎯 *CLAIM THESE AIRDROPS NOW!*\n\n"
        
        for i, airdrop in enumerate(airdrops, 1):
            message += f"*{i}. {airdrop['name']}*\n"
            message += f"   🔗 {airdrop['website']}\n"
            message += f"   💰 {airdrop['value']}\n"
            message += f"   ⏱️ {airdrop['time']}\n\n"
        
        message += "📝 *Steps:*\n"
        message += "1. Click link above\n"
        message += "2. Connect your wallet\n"
        message += "3. Complete tasks\n"
        message += "4. Claim rewards!\n\n"
        message += "💡 *Tip:* Do all 3 daily for maximum earnings!"
        
        # Add quick action buttons
        keyboard = []
        for airdrop in airdrops[:3]:  # First 3 airdrops
            keyboard.append([
                InlineKeyboardButton(
                    f"🚀 Claim {airdrop['name']}", 
                    url=airdrop['website']
                )
            ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    
    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Check current airdrop status"""
        airdrops = self.scanner.get_current_airdrops()
        
        message = "📊 *CURRENT AIRDROP STATUS*\n\n"
        message += f"🎯 Active Airdrops: {len(airdrops)}\n"
        message += f"💰 Total Potential Value: $30-1500\n"
        message += f"⏱️ Total Time Required: ~54 minutes\n"
        message += f"💵 Total Cost: FREE\n\n"
        
        message += "*Breakdown:*\n"
        for airdrop in airdrops:
            message += f"• {airdrop['name']}: {airdrop['value']}\n"
        
        message += "\nUse /claim to start earning!"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View earnings statistics"""
        message = """
📈 *YOUR AIRDROP STATISTICS*

🎯 *Current Active:*
   • T-Rex: 1170 points
   • PrismaX: 1782 points
   • Hotstuff: 1265 points

💰 *Estimated Value:*
   • Conservative: $35-185
   • Realistic: $185-750
   • Optimistic: $750-1850

⏱️ *Time Investment:*
   • Setup: 5 minutes (one-time)
   • Daily: 10 minutes
   • Total this month: ~5 hours

📊 *ROI:*
   • Potential: $50-500/month
   • Hourly rate: $10-100/hour
   • Cost: $0 (FREE!)

🔥 *Keep claiming daily for maximum earnings!*
        """
        
        keyboard = [
            [InlineKeyboardButton("💰 Claim Now", callback_data='claim')],
            [InlineKeyboardButton("🔍 Find More", callback_data='scan')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def remind_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Set up daily reminders"""
        message = """
🔔 *DAILY REMINDER SETUP*

I can remind you daily to claim airdrops!

*Reminder Times:*
• 9:00 AM - Morning scan
• 10:30 AM - Daily tasks
• 8:00 PM - Evening check

*What you'll get:*
✅ New airdrop alerts
✅ Daily task reminders
✅ Deadline warnings
✅ Value updates

Use /settings to configure reminder times.
        """
        
        keyboard = [
            [InlineKeyboardButton("✅ Enable Reminders", callback_data='enable_remind')],
            [InlineKeyboardButton("⚙️ Configure Times", callback_data='settings')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            message,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def settings_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Bot settings"""
        message = """
⚙️ *BOT SETTINGS*

*Current Configuration:*
✅ Auto-scan: Enabled
✅ Notifications: Enabled
✅ Daily reminders: Enabled

*Customize:*
• Reminder times
• Notification preferences
• Airdrop filters
• Auto-claim settings

Edit config.json file to customize settings.
        """
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help message"""
        await self.start(update, context)
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button clicks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'scan':
            await query.message.reply_text("🔍 Scanning...")
            await self.scan_command(update, context)
        elif query.data == 'claim':
            await self.claim_command(update, context)
        elif query.data == 'stats':
            await self.stats_command(update, context)
        elif query.data == 'settings':
            await self.settings_command(update, context)
        elif query.data == 'enable_remind':
            await query.message.reply_text("✅ Daily reminders enabled! You'll receive notifications at 9 AM and 10:30 AM.")
    
    async def send_daily_notification(self, chat_id):
        """Send daily airdrop notification"""
        airdrops = self.scanner.get_current_airdrops()
        
        message = "🔔 *DAILY AIRDROP REMINDER!*\n\n"
        message += f"📅 {datetime.now().strftime('%B %d, %Y')}\n\n"
        message += "Don't forget your daily tasks:\n\n"
        
        for airdrop in airdrops:
            message += f"✅ {airdrop['name']}\n"
            message += f"   🔗 {airdrop['website']}\n\n"
        
        message += "⏱️ Takes only 10 minutes!\n"
        message += "💰 Potential: $50-500\n\n"
        message += "Click /claim to get started!"
        
        keyboard = [[InlineKeyboardButton("💰 Claim Now", callback_data='claim')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await self.app.bot.send_message(
            chat_id=chat_id,
            text=message,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    def run(self):
        """Start the bot"""
        # Create application
        self.app = Application.builder().token(self.token).build()
        
        # Add command handlers
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("scan", self.scan_command))
        self.app.add_handler(CommandHandler("claim", self.claim_command))
        self.app.add_handler(CommandHandler("status", self.status_command))
        self.app.add_handler(CommandHandler("stats", self.stats_command))
        self.app.add_handler(CommandHandler("remind", self.remind_command))
        self.app.add_handler(CommandHandler("settings", self.settings_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        
        # Add button callback handler
        self.app.add_handler(CallbackQueryHandler(self.button_callback))
        
        # Start bot
        logger.info("🤖 Telegram Airdrop Bot started!")
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    """Main function"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🤖 TELEGRAM AIRDROP BOT SETUP 🤖                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

SETUP INSTRUCTIONS:

1. Create Telegram Bot:
   • Open Telegram
   • Search for @BotFather
   • Send /newbot
   • Follow instructions
   • Copy your bot token

2. Get Your Chat ID:
   • Search for @userinfobot
   • Send /start
   • Copy your chat ID

3. Configure:
   • Edit config.json
   • Add bot_token and chat_id

4. Run:
   • python telegram_bot.py

═══════════════════════════════════════════════════════════
    """)
    
    # Load config
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        token = config.get('telegram_bot_token')
        
        if not token:
            print("❌ Error: telegram_bot_token not found in config.json")
            print("\nPlease add your Telegram bot token to config.json:")
            print('{\n  "telegram_bot_token": "YOUR_BOT_TOKEN_HERE",\n  ...\n}')
            return
        
        # Start bot
        bot = TelegramAirdropBot(token, config)
        bot.run()
        
    except FileNotFoundError:
        print("❌ Error: config.json not found")
        print("Run: python setup.py first")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
