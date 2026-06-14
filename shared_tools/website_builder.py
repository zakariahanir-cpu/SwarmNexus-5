import os

def create_web_project(agent_name, project_name, files):
    """
    ينشئ مشروع موقع ويب جديد في مجلد الوكيل.
    files: قاموس يحتوي على أسماء الملفات ومحتوياتها.
    """
    project_path = f"/home/ubuntu/agents/{agent_name}/{project_name}"
    os.makedirs(project_path, exist_ok=True)
    
    created_files = []
    for filename, content in files.items():
        file_path = os.path.join(project_path, filename)
        with open(file_path, "w") as f:
            f.write(content)
        created_files.append(filename)
    
    return f"Project '{project_name}' created by {agent_name} with files: {', '.join(created_files)}"

if __name__ == "__main__":
    # Test
    test_files = {
        "index.html": "<html><body><h1>Hello World</h1></body></html>",
        "style.css": "body { background-color: #f0f0f0; }"
    }
    print(create_web_project("agent_alpha", "test_site", test_files))
  
