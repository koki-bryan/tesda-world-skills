import json 
import requests

overall_result=[]
fp = "/home/competitor/project/prompts/few_shot_results.json"
OLLAMA_URL = 'http://localhost:11434/api/generate'

def prompt_inject(user_prompt:str):
    return f"""Your job is to determine which category the User prompt fits best. 
               The categories are only: praise, question, complaint
               Respond only in JSON.

Example:
(User Prompt):
prompt: The service at the restaurant was extremely slow
(AI):
{{category : complaint}}

(User Prompt):
prompt: what is the weather today?
(AI):
{{category : question}}

(User Prompt):
prompt: It is a nice service and experience
(AI):
{{category : praise}}


(User prompt):
prompt: {user_prompt} 
(AI):
{{category : }}

"""

messages=[
    "You are so Intelligent Sean!",
    "I love the service that we experienced",
    "I do not like my item, the parcel is broken",
    "I am not coming back in this place, the service is bad",
    "How do i go to the market?"
]


for mess in messages:
    
    payload={
        "model":"mistral",
        "prompt": prompt_inject(mess),
        "stream": False
    }
    
    res = requests.post(OLLAMA_URL, json=payload)
    d = res.json()
    data = d.get('response')
    
    print(data)
    overall_result.append(data)

with open(fp,"a") as f:
    json.dump(overall_result, f)
    