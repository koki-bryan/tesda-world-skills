import json, requests

results=[]
ollama_api = "http://localhost:11434/api/generate"
files=["test.py", "test.js", "test.java"]


def read_file(file:str):
    path=f"/home/competitor/data/code_snippets/{file}"
    
    try:
        with open(path, "r") as r:
            read = r.read()
        
        return read
    except FileNotFoundError:
        return f"Error: {file} not found."
    except Exception as e:
        return f"An error occurred: {e}"
    

def basic_prompt(code:str):
    payload={
        "model": "mistral",
        "prompt": f"Find and fix the bug in this code: {code}",
        "stream": False
    }
    
    r=requests.post(ollama_api, json=payload)
    data=r.json()
    
    return data['response']


def engineered_prompt(code:str):
    payload={
        "model": "mistral",
        "prompt": f"""You are a beginner-friendly programming debugging assistant. 
        Analyze the following Python code carefully.
        
        Tasks:
        1. Identify the bug
        2. Explain why the issue occurs
        3. Provide corrected code
        4. Keep explanations concise and beginner-friendly
        Code:{code}""",
        "stream": False
    }
    
    r=requests.post(ollama_api, json=payload)
    data=r.json()
    
    return data['response']

for i in files:
    file=i
    read_code=read_file(file)
    basic_result=basic_prompt(read_code)
    eng_result=engineered_prompt(read_code)
    
    result={
        "file": file,
        "basic_response": basic_result,
        "engineered_result": eng_result
    }
    
    results.append(result)
    

dump_path="/home/competitor/project/prompts/prompt_comparison.json"
with open(dump_path, "w") as f:
    json.dump(results, f, indent=4)