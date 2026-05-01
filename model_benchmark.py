import requests, time, json

# Array creation similar to JS, syntax =[]
PROMPTS=[
    "What is the capital of Philippines",
    "Write a 5-word sentence about a robot eating pizza.",
    "if all Bloops are Razzies and all Razzies are Lulus, are all Bloops definitely Lulus?",
    "What is the chemical symbol for gold?",
    "Translate 'Where is the library' into Filipino"
]

ollama_url="http://localhost:11434/api/generate"
MODELS=["mistral", "phi3", "llama3.2"]
result_output=[]

for i in MODELS:
    print(f"-----{i.capitalize()}-----")
    
    for j, h in enumerate(PROMPTS):
        payload={
            "model":i,
            "prompt":h,
            "stream":False
        }
        start=time.time()
        r=requests.post(ollama_url, json=payload) #you need to convert the dictionary to json
        data=r.json()
        end=time.time()
        
        responseTime=(end-start)
        
        #Compiling the results of each model
        result_payload={
            "model":i,
            "prompt":h,
            "response":data['response'],
            "response_time":responseTime,
            "tokens": data['eval_count'],
        }
        result_output.append(result_payload)
        
        print(f"[{j+1}/5] {h} | {responseTime:.2f}s {data['eval_count']} tokens")
        
output_path="/home/competitor/project/benchmark_results.json"
with open(output_path, "w") as f:
    json.dump(result_output, f, indent=4)