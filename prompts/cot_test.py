import requests, json

problems=["John has a meeting at 3:00 PM. It takes 25 minutes to drive there. He also needs 15 minutes to prepare before leaving. If he wants to arrive 10 minutes early, what time should he start preparing?",
          "A warehouse has 450 units of a product. On Monday, they ship out 1/3 of the stock. On Tuesday, they receive a new shipment that increases the remaining stock by 20%. How many units are in the warehouse by Tuesday evening?",
          "What do you think would be next number in sequence [1, 4, 9, 16, 25, 36, 49, _]"]

cot_instruction="Solve the following problem step-by-step. Show your reasoning clearly before giving the final answer."
cot_problems=[f"{cot_instruction} John has a meeting at 3:00 PM. It takes 25 minutes to drive there. He also needs 15 minutes to prepare before leaving. If he wants to arrive 10 minutes early, what time should he start preparing?",
          f"{cot_instruction} A warehouse has 450 units of a product. On Monday, they ship out 1/3 of the stock. On Tuesday, they receive a new shipment that increases the remaining stock by 20%. How many units are in the warehouse by Tuesday evening?",
          f"{cot_instruction} What do you think would be next number in sequence [1, 4, 9, 16, 25, 36, 49, _]"]

ollama_api = "http://localhost:11434/api/generate"
results=[]

for i in range(len(problems)):
    print(f"Start {i}")
    normal_payload={
        "model": "mistral",
        "prompt": problems[i],
        "stream": False
    }
    
    r=requests.post(ollama_api, json=normal_payload)
    data=r.json()
    normal_prompt=data['response']
    
    cot_payload={
        "model": "mistral",
        "prompt": cot_problems[i],
        "stream": False
    }
    
    j=requests.post(ollama_api, json=cot_payload)
    cot_data=j.json()
    cot_prompt=cot_data['response']
    
    result_prompts={
        "problem": problems[i],
        "basic_prompt": normal_prompt,
        "cot_prompt": cot_prompt
    }
    results.append(result_prompts)
    
dump_path="/home/competitor/project/prompts/cot_comparison.json"

with open(dump_path, "w") as f:
    json.dump(results, f, indent=4)