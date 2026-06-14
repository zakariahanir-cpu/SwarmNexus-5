import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from shared_tools.agent_engine import Agent

api_key = os.getenv("BETA_GROQ")

class AgentBeta(Agent):
    def __init__(self):
        super().__init__("agent_beta", api_key)

if __name__ == "__main__":
    agent = AgentBeta()
    print(f"--- {agent.name} is online ---")
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        result = agent.perform_task(task)
        print(result)
    else:
        agent.perform_task("تحقق من سجل الرسائل وقم بتحديث قاعدة معرفتك أو ابدأ ببناء ميزة جديدة في موقعك.")
      
