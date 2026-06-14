import os
import json

# تحديد المسار الأساسي للمشروع تلقائياً
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Agent:
    def __init__(self, agent_name, api_key=None, *args, **kwargs):
        self.name = agent_name
        self.api_key = api_key
        
        # مسار الذاكرة الديناميكي الذي أصلحناه سابقاً
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
        """
        تنفيذ المهمة وطباعة مخرجاتها مباشرة في الـ Terminal ليراها المستخدم
        """
        # طباعة بداية تنفيذ المهمة للاستدلال
        print(f"[{self.name}] Starting task: {task_description}")
        
        response = ""
        try:
            # ------------------------------------------------------------
            # كود الاتصال بـ Groq API وتوليد الرد الخاص بك يوضع هنا
            # كمثال (تأكد من مطابقتة لطريقة استدعائك للـ API):
            # response = self.call_llm_logic(task_description)
            # ------------------------------------------------------------
            
            # (هذا سطر افتراضي، استبدله بمتغير الاستجابة الفعلي من نموذجك)
            response = f"تم تنفيذ المهمة بنجاح بواسطة {self.name}." 
            
            # ✨ الإضافة السحرية: طباعة الاستجابة مباشرة هنا ليظهر في سجلات GitHub
            print(f"[{self.name}] Task Execution Output:\n{response}")
            
        except Exception as e:
            print(f"[{self.name}] Self-healing triggered due to error: {str(e)}")
            from shared_tools.learner import save_knowledge
            save_knowledge(self.name, task_description, "Failure -> Self-Healed", str(e))
            response = f"Error encountered but self-healed: {str(e)}"
            
        # حفظ الذاكرة تلقائياً بعد انتهاء المهمة
        self.save_memory()
        
        return response
        
