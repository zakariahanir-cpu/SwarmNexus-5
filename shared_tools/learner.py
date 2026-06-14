import json
import os

# تحديد المسار الأساسي للمشروع (المجلد الأب للمجلد الحالي shared_tools)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# تحديد مسار قاعدة المعرفة داخل مجلد المشروع
KNOWLEDGE_BASE_FILE = os.path.join(BASE_DIR, "knowledge_base", "learned_knowledge.json")

def ensure_knowledge_dir():
    """التأكد من أن المجلد موجود قبل الحفظ"""
    directory = os.path.dirname(KNOWLEDGE_BASE_FILE)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def save_knowledge(agent_name, task, outcome, solution):
    """
    يحفظ المعرفة المكتسبة من قبل الوكيل.
    """
    ensure_knowledge_dir()  # التأكد من وجود المجلد
    
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
        json.dump(knowledge, f, indent=4, ensure_ascii=False)
        
    return f"Knowledge saved by {agent_name} for task: {task}"

def get_knowledge(query):
    """
    يبحث في قاعدة المعرفة عن حلول سابقة.
    """
    if not os.path.exists(KNOWLEDGE_BASE_FILE):
        return []
    
    with open(KNOWLEDGE_BASE_FILE, "r") as f:
        try:
            knowledge = json.load(f)
        except json.JSONDecodeError:
            return []
    
    # بحث بسيط
    matches = [k for k in knowledge if query.lower() in k['task'].lower() or query.lower() in k['solution'].lower()]
    return matches
    
