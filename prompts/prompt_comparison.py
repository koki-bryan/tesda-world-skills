import json
import requests
import os

overall_result=[]
fp = "/home/competitor/project/prompts/prompt_comparison.json"
OLLAMA_URL = 'http://localhost:11434/api/generate'

def read_file(file:str):
    base_dir = "/home/competitor/data/code_snippets/"
    abs_path = os.path.abspath(base_dir)
    
    req_dir = os.path.abspath(os.path.join(base_dir, file))
    
    if not req_dir.startswith(abs_path):
        return "Restricted"
    
    try:
        with open(req_dir, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        return "file not found"
    except Exception as e:
        return f"Error {str(e)}"

def prompt_inject(user_prompt:str):
    return f"""You are a Senior Software engineer reviewing for buggy codes. Your goal is to identify and resolve the bugs found in the follwing files. Respond only with the solved output and concise explanation on what went wrong.
    Code: 
    {user_prompt}"""
    
buggy_files = ['buggy1.py', 'buggy2.py', 'buggy3.py']
for i in buggy_files:
    
    payload={
        "model": "mistral",
        "prompt": prompt_inject(read_file(i)),
        "stream": False
    }
    
    r = requests.post(OLLAMA_URL, json=payload)
    d = r.json()
    data = d.get('response')
    
    overall_result.append({"engr_prompt" : data})
    
    payload1={
        "model": "mistral",
        "prompt": read_file(i),
        "stream": False
    }
    
    r1 = requests.post(OLLAMA_URL, json=payload1)
    d1 = r1.json()
    data1 = d1.get('response')
    
    overall_result.append({"basic_prompt":data1})
    
with open(fp, 'w') as f:
    json.dump(overall_result, f)
    
    
    
    
