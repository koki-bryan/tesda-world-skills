import json
import requests

result=[]
OLLAMA_URL = 'http://localhost:11434/api/generate'
fp = "/home/competitor/project/prompts/cot_comparison.json"

def prompt_inject(prompt:str):
     
    SYSTEM=f"""
        Think before you answer, Do not rush, take as much time you want. if you do not know the answer, simply respond 'I don't know'
        prompt: {prompt}
    """
    
    return SYSTEM

prompts=[
    "what is the 1/3 of 20",
    "what is the next in sequence 2, 4, 6, 8, 10, _",
    "Evaluate the expression 8 * 2 + (9/0)"
]

for i in prompts:
    
    payload={
        "model": "mistral",
        "prompt": prompt_inject(i),
        "stream": False
    }
    
    r = requests.post(OLLAMA_URL, json=payload)
    d = r.json()
    data = d.get('response')
    
    payload2={
        "model":"mistral",
        "prompt": i,
        "stream": False
    }
    
    rr = requests.post(OLLAMA_URL, json=payload2)
    dd = rr.json()
    dData = dd.get('response')
    
    result.append({"prompt": i, "cot_res": data, "basic_res": dData})

with open(fp, 'w') as f:
    json.dump(result, f)