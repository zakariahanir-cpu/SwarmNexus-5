import os
import json

# تحديد المسار الأساسي للمشروع تلقائياً (المجلد الأب لـ shared_tools)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Agent:
    def __init__(self, agent_name):
        self.name = agent_name
        
        # تصحيح مسار الذاكرة ليكون ديناميكياً ونسبياً للمشروع
        self.memory_path = os.path.join(BASE_DIR, "agents", self.name, "memory.json")
        
        # هنا يمكنك ترك أي متغيرات أخرى كانت لديك في الـ __init__ القديم مثل:
        self.memory = {} 

    def save_memory(self):
        """
        يحفظ ذاكرة الوكيل بشكل آمن ويضمن إنشاء المجلدات إن لم تكن موجودة.
        """
        # التأكد من إنشاء مجلد الوكيل تلقائياً في بيئة الـ GitHub Actions
        directory = os.path.dirname(self.memory_path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        # استخدام الذاكرة الموجودة في الكائن، وإذا لم تكن موجودة نضع قاموساً فارغاً
        memory_data = getattr(self, 'memory', {}) 
        
        with open(self.memory_path, "w") as f:
            json.dump(memory_data, f, indent=4, ensure_ascii=False)
            
        return f"Memory saved for {self.name}"

    def perform_task(self, task_description):
        """
        تنفيذ المهمة (تأكد من الإبقاء على دالتك القديمة كما هي، 
        هذا مجرد هيكل توضيحي للسياق الذي استدعى الخطأ عندك)
        """
        try:
            # كود تنفيذ المهمة الخاص بك...
            pass
        except Exception as e:
            # دالة العلاج الذاتي التي تطلق الحفظ عند الفشل
            print(f"[{self.name}] Self-healing triggered...")
            # هنا يتم استدعاء save_knowledge من الملف الآخر (وقد أصلحناه سابقاً)
            from shared_tools.learner import save_knowledge
            save_knowledge(self.name, task_description, "Failure -> Self-Healed", str(e))
            
        # السطر 78 الذي تسبب في الخطأ الأخير أصبح الآن آمناً ومحمياً بـ ensure_ok
        self.save_memory()
        
