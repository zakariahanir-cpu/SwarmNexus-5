import os
import json
import requests
from shared_tools.duckduckgo_search import search_duckduckgo
from shared_tools.messenger import send_message, read_messages
from shared_tools.website_builder import create_web_project
from shared_tools.learner import save_knowledge, get_knowledge

class Agent:
    def __init__(self, name, api_key):
        self.name = name
        self.api_key = api_key
        self.model = "llama-3.1-70b-versatile" # Groq 70b
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.memory_path = f"/home/ubuntu/agents/{name}/memory.json"
        self.history = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                return json.load(f)
        return []

    def save_memory(self):
        with open(self.memory_path, "w") as f:
            json.dump(self.history, f, indent=4)

    def call_llm(self, prompt, system_prompt="You are a powerful AI agent with self-learning and self-healing capabilities."):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error calling LLM: {str(e)}"

    def perform_task(self, task_description):
        print(f"[{self.name}] Performing task: {task_description}")
        
        # 1. Search knowledge base
        past_knowledge = get_knowledge(task_description)
        knowledge_context = ""
        if past_knowledge:
            knowledge_context = "Past relevant knowledge: " + json.dumps(past_knowledge)

        # 2. Decision making
        system_prompt = f"""
        You are {self.name}, a powerful AI agent. 
        You have tools: search_duckduckgo, send_message, read_messages, create_web_project, save_knowledge.
        Your goal is to complete the task. If you fail, analyze why and try to fix yourself (Self-Healing).
        {knowledge_context}
        """
        
        response = self.call_llm(task_description, system_prompt)
        
        # 3. Handle Self-Healing / Learning
        if "error" in response.lower() or "fail" in response.lower():
            print(f"[{self.name}] Self-healing triggered...")
            # Try to search for a solution
            search_results = search_duckduckgo(f"how to fix {task_description}")
            healing_prompt = f"I failed the task: {task_description}. Search results: {search_results}. How can I fix this and complete the task?"
            response = self.call_llm(healing_prompt, system_prompt)
            save_knowledge(self.name, task_description, "Failure -> Self-Healed", response)
        else:
            save_knowledge(self.name, task_description, "Success", response)
            
        self.history.append({"task": task_description, "response": response})
        self.save_memory()
        return response

    def ask_for_help(self, title, subject, content):
        return send_message(self.name, title, subject, content)

    def check_messages(self):
        return read_messages()
  
