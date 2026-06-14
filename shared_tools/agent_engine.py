import os
import json

# تأكد من إضافة هذا السطر في أعلى الملف لتحديد مسار المشروع الأساسي
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# داخل كلاس AgentEngine أو الكلاس المسؤول:
class AgentEngine:
    def __init__(self, agent_name, ...): # أضف بقية المتغيرات الخاصة بك هنا
        self.name = agent_name
        
        # تصحيح مسار الذاكرة ليكون ديناميكياً ونسبياً للمشروع
        self.memory_path = os.path.join(BASE_DIR, "agents", self.name, "memory.json")
        
        # بقية كود الـ __init__ الخاص بك...

    def save_memory(self):
        """
        يحفظ ذاكرة الوكيل بشكل آمن ويضمن إنشاء المجلدات إن لم تكن موجودة.
        """
        # التأكد من إنشاء مجلد الوكيل تلقائياً في بيئة الـ GitHub Actions
        directory = os.path.dirname(self.memory_path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        # البيانات المراد حفظها (قم بتعديلها لتناسب الكود الأصلي لديك إن كانت تختلف)
        memory_data = getattr(self, 'memory', {}) 
        
        with open(self.memory_path, "w") as f:
            json.dump(memory_data, f, indent=4, ensure_ascii=False)
            
