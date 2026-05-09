import requests 
import json

messages = [
    "Could you clarify if the annual subscription includes access to the mobile app?",
    "The checkout page keeps crashing every time I try to enter my shipping address.",
    "Your customer support team is incredible; they resolved my issue in under five minutes!",
    "Why am I being charged a convenience fee that wasn't mentioned during signup?",
    "The dark mode implementation is flawless and much easier on my eyes during late shifts."
]

ollama_api = "http://localhost:11434/api/generate"

responses=[]

for i, message in enumerate(messages):
    
    payload = {
        "model": "mistral",
        "prompt": f"""Classify the user input into ONLY one of these categories:
- complaint
- question
- praise

Respond ONLY in JSON format:
Input:
<message>
Output:
{{
    "category":<label>
}}

Input:
"You are so great at doing your job"
Output:
{{
    "category":"praise"
}}

Input:
"Do you offer a student discount for the monthly subscription?"
Output:
{{
    "category":"question"
}}

Input:
"The delivery was two days late and the box was crushed."
Output:
{{
    "category":"complaint"
}}

Input:
"{message}"
Output:""",
        "stream": False 
    }

    response = requests.post(ollama_api, json=payload)
    result = response.json()
    parsed_output= json.loads(result['response'])
    
    res={
        "user_input": message,
        "category": parsed_output['category']
    }
    responses.append(res)
    
    
    print(f"Message {i+1}: {message}")
    print(f"Model response: {parsed_output['category']}\n")

path="/home/competitor/project/prompts/few_shot_results.json"
with open(path, "w") as f:
    json.dump(responses, f, indent=4)