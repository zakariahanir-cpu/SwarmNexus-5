import os
import sys

# إضافة المسار الرئيسي للمشروع لاستيراد الأدوات المشتركة
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from shared_tools.agent_engine import Agent

# المفتاح الخاص بالوكيل Alpha
api_key = os.getenv("ALPHA_GROQ")

class AgentAlpha(Agent):
    def __init__(self):
        super().__init__("agent_alpha", api_key)

if __name__ == "__main__":
    agent = AgentAlpha()
    print(f"--- {agent.name} is online ---")
    
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        result = agent.perform_task(task)
        print(result)
    else:
        # مهمة افتراضية للتعلم الذاتي في غياب مدخلات
        agent.perform_task("تحقق من سجل الرسائل وقم بتحديث قاعدة معرفتك أو ابدأ ببناء ميزة جديدة في موقعك.")
      
