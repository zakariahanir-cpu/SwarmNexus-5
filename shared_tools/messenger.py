import json
import os
from datetime import datetime

MESSAGES_FILE = "/home/ubuntu/communication_hub/messages/log.txt"

def send_message(sender, title, subject, content):
    """
    يرسل رسالة إلى ملف الرسائل المخصص.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"--- MESSAGE START ---\n"
    message += f"Date: {timestamp}\n"
    message += f"Sender: {sender}\n"
    message += f"Title: {title}\n"
    message += f"Subject: {subject}\n"
    message += f"Content: {content}\n"
    message += f"--- MESSAGE END ---\n\n"
    
    with open(MESSAGES_FILE, "a") as f:
        f.write(message)
    return f"Message sent from {sender} at {timestamp}"

def read_messages():
    """
    يقرأ جميع الرسائل من ملف الرسائل.
    """
    if not os.path.exists(MESSAGES_FILE):
        return "No messages yet."
    with open(MESSAGES_FILE, "r") as f:
        return f.read()

if __name__ == "__main__":
    # Test
    print(send_message("Agent Alpha", "Need Help", "CSS Layout", "I need help with a flexbox layout issue."))
    print(read_messages())
  
