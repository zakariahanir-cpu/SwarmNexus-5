import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Agent:
    # أضفنا api_key و *args و **kwargs لكي يقبل أي متغيرات يرسلها الوكيل دون مشاكل
    def __init__(self, agent_name, api_key=None, *args, **kwargs):
        self.name = agent_name
        self.api_key = api_key
        
        # مسار الذاكرة الديناميكي
        self.memory_path = os.path.join(BASE_DIR, "agents", self.name, "memory.json")
        self.memory = {} 

    def save_memory(self):
        """
        يحفظ ذاكرة الوكيل بشكل آمن ويضمن إنشاء المجلدات إن لم تكن موجودة.
        """
        directory = os.path.dirname(self.memory_path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        memory_data = getattr(self, 'memory', {}) 
        
        with open(self.memory_path, "w") as f:
            json.dump(memory_data, f, indent=4, ensure_ascii=False)
            
        return f"Memory saved for {self.name}"

    def perform_task(self, task_description):
        # هذا الجزء اتركه كما هو في كودك الأصلي
        pass 
