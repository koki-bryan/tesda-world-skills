import requests
import json
import time
from datetime import datetime

conversation_history=[]
agent_log=[]
agent_results=[]
while True:
    prompt=input(">>> ")
    
    start = time.time()
    if prompt.lower() == 'exit':
        break
    if prompt.lower() == 'history':
        print(conversation_history)
    
    SYSTEM = f"You are an agentic AI with access to these tools: calculate, weather tool and file reader tool if a user prompts for calculation simply respond in this format: calculator. if a user prompts for asking a question related to the weather respond: weather tool. if a user prompts for asking to open or read a file simply respond: file reader. If no tool available for the user prompt, respond: no tool. Example: User prompt: What is the Weather in philippines? AI: weather tool. user prompt: What is 1250 multiplied by 678? AI: calculator . User prompt: read files.txt. AI: file reader User prompt: {prompt}"
    
    payload={
        "model" : "mistral",
        "prompt" : SYSTEM,
        "stream" : False
    }
    
    r = requests.post("http://localhost:11434/api/generate", json=payload)
    data = r.json()
    end = time.time()
    
    total_time = end - start
    conversation_history.append({"user_prompt": prompt, "response": data.get('response')})
    agent_log.append({"user_input":prompt, "tool_used": data.get('response'), "final_response": data.get('response')})
    agent_results.append(f"{prompt} - {data.get('response')}")
    

with open("/home/competitor/project/agent_log.json", "a") as f:
    json.dump(agent_log, f, indent=4)

with open("/home/competitor/project/agent_test_results.txt", "a") as f:
    json.dump(agent_results, f)
    
