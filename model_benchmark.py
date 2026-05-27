import requests, json, time

prompts=[
    "why is the sky blue?",
    "how to learn something fast?",
    "what ai AI and ML?",
    "how can I learn AI",
    "what are you?"
]

models=["mistral", "llama3.2", "phi3"]

OLLAMA_URL='http://localhost:11434/api/generate'

overall_result=[]

for model in models:
    print(model)
    
    for count, prompt in enumerate(prompts):
        start_time = time.time()
        payload={
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        r= requests.post(OLLAMA_URL, json=payload)
        data = r.json()
        end_time = time.time()
        
        response = data.get('response')
        tokens = data.get('eval_count')
        overall_time = end_time - start_time
        
        overall_result.append({"prompt": prompt, "response": response, "tokens": tokens, "time":overall_time})

with open('/home/competitor/project/benchmark_results.json', 'w') as f:
    json.dump(overall_result, f, indent=4)