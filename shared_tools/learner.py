import json
import os

KNOWLEDGE_BASE_FILE = "/home/ubuntu/knowledge_base/learned_knowledge.json"

def save_knowledge(agent_name, task, outcome, solution):
    """
    يحفظ المعرفة المكتسبة من قبل الوكيل.
    """
    knowledge = []
    if os.path.exists(KNOWLEDGE_BASE_FILE):
        with open(KNOWLEDGE_BASE_FILE, "r") as f:
            try:
                knowledge = json.load(f)
            except json.JSONDecodeError:
                knowledge = []
    
    knowledge.append({
        "agent": agent_name,
        "task": task,
        "outcome": outcome,
        "solution": solution
    })
    
    with open(KNOWLEDGE_BASE_FILE, "w") as f:
        json.dump(knowledge, f, indent=4)
    return f"Knowledge saved by {agent_name} for task: {task}"

def get_knowledge(query):
    """
    يبحث في قاعدة المعرفة عن حلول سابقة.
    """
    if not os.path.exists(KNOWLEDGE_BASE_FILE):
        return []
    
    with open(KNOWLEDGE_BASE_FILE, "r") as f:
        knowledge = json.load(f)
    
    # بحث بسيط (يمكن تحسينه لاحقاً باستخدام نموذج لغوي)
    matches = [k for k in knowledge if query.lower() in k['task'].lower() or query.lower() in k['solution'].lower()]
    return matches
  
