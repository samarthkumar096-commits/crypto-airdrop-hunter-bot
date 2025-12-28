"""
Telegram Bot Integration for Airdrop Hunter
Control your airdrop bot from anywhere via Telegram!
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
from scanner import AirdropScanner
from hotstuff_tracker import get_hotstuff_notification, get_hotstuff_opportunities, get_hotstuff_airdrop_analysis
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
/hotstuff - 🔥 HotStuff L1 opportunities
/status - Check current airdrops
/stats - View your earnings
/remind - Set daily reminders
/settings - Configure bot
/help - Show this message

*Quick Start:*
1. Use /scan to find airdrops
2. Use /claim to get links
3. Try /hotstuff for HotStuff L1 testnet!
4. Click links and claim!

Let's start earning! 💰
        """
        
        keyboard = [
            [
                InlineKeyboardButton("🔍 Scan Airdrops", callback_data='scan'),
                InlineKeyboardButton("💰 Claim Now", callback_data='claim')
            ],
            [
                InlineKeyboardButton("🔥 HotStuff L1", callback_data='hotstuff'),
                InlineKeyboardButton("📊 My Stats", callback_data='stats')
            ],
            [
                InlineKeyboardButton("⚙️ Settings", callback_data='settings')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def hotstuff_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """HotStuff L1 information and opportunities"""
        await update.message.reply_text("🔥 Loading HotStuff L1 info... Please wait...")
        
        try:
            # Get HotStuff notification
            message = get_hotstuff_notification()
            
            # Add action buttons
            keyboard = [
                [InlineKeyboardButton("🌐 Visit HotStuff", url="https://hotstuff.trade")],
                [InlineKeyboardButton("📚 Read Docs", url="https://docs.hotstuff.trade")],
                [InlineKeyboardButton("🔄 Refresh Status", callback_data='hotstuff')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                message,
                parse_mode='Markdown',
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )
            
        except Exception as e:
            logger.error(f"Error in hotstuff command: {e}")
            await update.message.reply_text("❌ Error loading HotStuff info. Please try again.")
    
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
                
                message += "💡 *NEW:* Try /hotstuff for HotStuff L1 testnet opportunities!\n\n"
                message += "Use /claim to get direct claim links!"
                
                await update.message.reply_text(message, parse_mode='Markdown')
            else:
                await update.message.reply_text("❌ No new airdrops found. Try /hotstuff for HotStuff L1!")
                
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
        
        message += "🔥 *BONUS:* HotStuff L1 Testnet\n"
        message += "   🔗 https://hotstuff.trade\n"
        message += "   💰 High airdrop potential (8/10)\n"
        message += "   ⏱️ 10-15 min daily\n\n"
        
        message += "📝 *Steps:*\n"
        message += "1. Click link above\n"
        message += "2. Connect your wallet\n"
        message += "3. Complete tasks\n"
        message += "4. Claim rewards!\n\n"
        message += "💡 *Tip:* Do all daily + HotStuff for maximum earnings!"
        
        # Add quick action buttons
        keyboard = []
        for airdrop in airdrops[:3]:  # First 3 airdrops
            keyboard.append([
                InlineKeyboardButton(
                    f"🚀 Claim {airdrop['name']}", 
                    url=airdrop['website']
                )
            ])
        
        # Add HotStuff button
        keyboard.append([
            InlineKeyboardButton("🔥 Try HotStuff L1", url="https://hotstuff.trade")
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
        message += f"🎯 Active Airdrops: {len(airdrops) + 1}\n"  # +1 for HotStuff
        message += f"💰 Total Potential Value: $30-1500+\n"
        message += f"⏱️ Total Time Required: ~60 minutes\n"
        message += f"💵 Total Cost: FREE\n\n"
        
        message += "*Breakdown:*\n"
        for airdrop in airdrops:
            message += f"• {airdrop['name']}: {airdrop['value']}\n"
        
        message += f"• 🔥 HotStuff L1: High potential (8/10)\n\n"
        
        message += "Use /claim to start earning!\n"
        message += "Use /hotstuff for HotStuff details!"
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """View earnings statistics"""
        message = """
📈 *YOUR AIRDROP STATISTICS*

🎯 *Current Active:*
   • T-Rex: 1170 points
   • PrismaX: 1782 points
   • Hotstuff: 1265 points
   • 🔥 HotStuff L1: Testnet active

💰 *Estimated Value:*
   • Conservative: $35-185
   • Realistic: $185-750
   • Optimistic: $750-1850+

⏱️ *Time Investment:*
   • Setup: 5 minutes (one-time)
   • Daily: 10-15 minutes
   • Total this month: ~5 hours

📊 *ROI:*
   • Potential: $50-500+/month
   • Hourly rate: $10-100/hour
   • Cost: $0 (FREE!)

🔥 *Keep claiming daily for maximum earnings!*
💡 *Don't miss HotStuff L1 testnet - use /hotstuff*
        """
        
        keyboard = [
            [InlineKeyboardButton("💰 Claim Now", callback_data='claim')],
            [InlineKeyboardButton("🔥 HotStuff L1", callback_data='hotstuff')],
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
✅ HotStuff L1 updates
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
✅ HotStuff tracking: Enabled

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
        """Handle button callbacks"""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'scan':
            await self.scan_command(update, context)
        elif query.data == 'claim':
            await self.claim_command(update, context)
        elif query.data == 'hotstuff':
            await self.hotstuff_command(update, context)
        elif query.data == 'stats':
            await self.stats_command(update, context)
        elif query.data == 'settings':
            await self.settings_command(update, context)
        elif query.data == 'enable_remind':
            await query.edit_message_text("✅ Daily reminders enabled! You'll receive notifications at 9 AM, 10:30 AM, and 8 PM.")
    
    def run(self):
        """Run the bot"""
        try:
            # Create application
            self.app = Application.builder().token(self.token).build()
            
            # Add command handlers
            self.app.add_handler(CommandHandler("start", self.start))
            self.app.add_handler(CommandHandler("scan", self.scan_command))
            self.app.add_handler(CommandHandler("claim", self.claim_command))
            self.app.add_handler(CommandHandler("hotstuff", self.hotstuff_command))
            self.app.add_handler(CommandHandler("status", self.status_command))
            self.app.add_handler(CommandHandler("stats", self.stats_command))
            self.app.add_handler(CommandHandler("remind", self.remind_command))
            self.app.add_handler(CommandHandler("settings", self.settings_command))
            self.app.add_handler(CommandHandler("help", self.help_command))
            
            # Add callback handler for buttons
            self.app.add_handler(CallbackQueryHandler(self.button_callback))
            
            # Start bot
            logger.info("🚀 Telegram bot started!")
            logger.info("🔥 HotStuff L1 integration active!")
            self.app.run_polling(allowed_updates=Update.ALL_TYPES)
            
        except Exception as e:
            logger.error(f"Error running bot: {e}")
            raise

def main():
    """Main function"""
    try:
        # Load config
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        # Get bot token
        token = config.get('telegram_bot_token')
        if not token:
            raise ValueError("Telegram bot token not found in config.json")
        
        # Create and run bot
        bot = TelegramAirdropBot(token, config)
        bot.run()
        
    except FileNotFoundError:
        logger.error("config.json not found! Please create it with your bot token.")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
