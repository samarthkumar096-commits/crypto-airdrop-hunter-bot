# MAI-UI Integration Module
# Integrates MAI-UI GUI agent with Telegram bot

import requests
import json
from typing import Dict, List, Optional

class MAIUIIntegration:
    """
    Integration with MAI-UI for GUI automation tasks
    """
    
    def __init__(self, api_base_url: str = "http://localhost:8000/v1", model_name: str = "MAI-UI-8B"):
        """
        Initialize MAI-UI integration
        
        Args:
            api_base_url: Base URL of MAI-UI vLLM server
            model_name: Model name (MAI-UI-2B or MAI-UI-8B)
        """
        self.api_base_url = api_base_url
        self.model_name = model_name
        self.headers = {
            "Content-Type": "application/json"
        }
    
    def check_availability(self) -> bool:
        """Check if MAI-UI service is available"""
        try:
            response = requests.get(f"{self.api_base_url}/models", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def execute_task(self, task: str, screenshot_path: Optional[str] = None) -> Dict:
        """
        Execute a GUI automation task using MAI-UI
        
        Args:
            task: Natural language task description
            screenshot_path: Optional path to current screenshot
            
        Returns:
            Dict with task execution results
        """
        
        # Prepare request payload
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": task
                }
            ],
            "temperature": 0.0,
            "max_tokens": 2048
        }
        
        # Add screenshot if provided
        if screenshot_path:
            # In real implementation, encode image to base64
            payload["images"] = [screenshot_path]
        
        try:
            response = requests.post(
                f"{self.api_base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "response": result["choices"][0]["message"]["content"],
                    "actions": self._parse_actions(result)
                }
            else:
                return {
                    "success": False,
                    "error": f"API error: {response.status_code}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _parse_actions(self, result: Dict) -> List[Dict]:
        """Parse actions from MAI-UI response"""
        # Parse the response to extract UI actions
        # This is simplified - actual implementation would be more complex
        actions = []
        
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        
        # Example action parsing
        if "click" in content.lower():
            actions.append({"type": "click", "description": content})
        elif "type" in content.lower():
            actions.append({"type": "type", "description": content})
        elif "scroll" in content.lower():
            actions.append({"type": "scroll", "description": content})
        
        return actions
    
    def get_supported_tasks(self) -> List[str]:
        """Get list of supported task types"""
        return [
            "App Navigation - Open and navigate apps",
            "Shopping - Search and purchase items",
            "Booking - Book tickets, hotels, restaurants",
            "Messaging - Send messages across apps",
            "Calendar - Manage calendar events",
            "Navigation - Plan routes and directions",
            "Data Collection - Extract information from apps",
            "Multi-app Workflows - Complex cross-app tasks"
        ]
    
    def format_task_for_telegram(self, task_result: Dict) -> str:
        """Format MAI-UI task result for Telegram message"""
        
        if not task_result.get("success"):
            return f"❌ Task failed: {task_result.get('error', 'Unknown error')}"
        
        message = "✅ **Task Completed!**\n\n"
        message += f"**Response:**\n{task_result['response']}\n\n"
        
        if task_result.get("actions"):
            message += "**Actions Performed:**\n"
            for i, action in enumerate(task_result["actions"], 1):
                message += f"{i}. {action['type'].title()}: {action['description']}\n"
        
        return message


# Example usage functions for Telegram bot

def create_mai_ui_handler():
    """Create MAI-UI handler for Telegram bot"""
    
    # Initialize MAI-UI integration
    mai_ui = MAIUIIntegration(
        api_base_url="http://localhost:8000/v1",
        model_name="MAI-UI-8B"
    )
    
    return mai_ui


def handle_automation_request(task: str) -> str:
    """
    Handle automation request from Telegram user
    
    Args:
        task: User's automation request
        
    Returns:
        Formatted response for Telegram
    """
    
    mai_ui = create_mai_ui_handler()
    
    # Check if MAI-UI is available
    if not mai_ui.check_availability():
        return """
❌ **MAI-UI Service Not Available**

MAI-UI is not running. To use GUI automation:

1. Deploy MAI-UI server
2. Start vLLM API service
3. Configure API endpoint

**Setup Guide:**
https://github.com/Tongyi-MAI/MAI-UI
        """
    
    # Execute task
    result = mai_ui.execute_task(task)
    
    # Format response
    return mai_ui.format_task_for_telegram(result)


# Example tasks that can be automated

EXAMPLE_TASKS = {
    "shopping": "Go to Taobao, search for 'wireless headphones', filter by price under 200 yuan, add top rated item to cart",
    "booking": "Open 12306, search for trains from Beijing to Shanghai tomorrow morning, show available tickets",
    "messaging": "Open WeChat, send message to 'Work Group' saying 'Meeting postponed to 3 PM'",
    "navigation": "Open Amap, plan route from current location to nearest Starbucks using public transport",
    "calendar": "Open Calendar, create event 'Team Meeting' tomorrow at 2 PM, invite team members",
    "multi_app": "Search 'iPhone 15' on Xiaohongshu, save top image, search same on Taobao, compare prices"
}


def get_example_tasks() -> str:
    """Get formatted example tasks for users"""
    
    message = "🤖 **MAI-UI Automation Examples:**\n\n"
    
    for category, task in EXAMPLE_TASKS.items():
        message += f"**{category.title()}:**\n"
        message += f"_{task}_\n\n"
    
    message += "💡 **Try your own task!**\n"
    message += "Just describe what you want to do naturally!"
    
    return message


# Integration info

def get_mai_ui_info() -> str:
    """Get MAI-UI integration information"""
    
    return """
🤖 **MAI-UI Integration**

**What is MAI-UI?**
AI agent that can control your phone/computer screen automatically!

**Capabilities:**
✅ App navigation
✅ Shopping automation
✅ Booking tickets
✅ Sending messages
✅ Calendar management
✅ Route planning
✅ Multi-app workflows

**How to Use:**
1. Deploy MAI-UI server (see setup guide)
2. Use `/automate <task>` command
3. MAI-UI executes task automatically
4. Get results in Telegram!

**Example:**
`/automate Book train from Beijing to Shanghai tomorrow`

**Setup Guide:**
https://github.com/Tongyi-MAI/MAI-UI

**Models Available:**
• MAI-UI-2B (on-device)
• MAI-UI-8B (small server)
• MAI-UI-32B (powerful server)

**Status:** 🔴 Not configured (setup required)
    """


if __name__ == "__main__":
    # Test integration
    print("MAI-UI Integration Module")
    print("=" * 50)
    
    # Show example tasks
    print(get_example_tasks())
    
    # Show integration info
    print("\n" + get_mai_ui_info())
