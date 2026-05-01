import requests, json, time

PROMPTS = [
    "What is artificial intelligence?",
    "Explain machine learning in simple terms.",
    "What is the capital of the Philippines?",
    "Write a haiku about technology.",
    "What are the benefits of renewable energy?"
]

MODELS = ["llama3.2", "mistral", "phi3"]
OLLAMA_URL = "http://localhost:11434/api/generate"

results = []
for model in MODELS:
    print(f"\n--- {model} ---")
    model_data = {"model": model, "responses": []}
    for i, p in enumerate(PROMPTS, 1):
        print(f"  [{i}/5] {p[:50]}...", end=" ", flush=True)
        start = time.time()
        try:
            r = requests.post(OLLAMA_URL, json={
                "model": model, "prompt": p, "stream": False
            }, timeout=120)
            r.raise_for_status()
            resp = r.json()
            elapsed = round(time.time() - start, 3)
            item = {
                "prompt": p,
                "response_time_seconds": elapsed,
                "output_tokens": resp.get("eval_count", 0),
                "input_tokens": resp.get("prompt_eval_count", 0),
                "response_preview": resp.get("response", "")[:100]
            }
            print(f"✓ {elapsed}s, {item['output_tokens']} tokens")
        except Exception as e:
            print(f"✗ ERROR: {e}")
            item = {"prompt": p, "error": str(e)}
        model_data["responses"].append(item)
    results.append(model_data)

with open("/home/competitor/project/benchmark_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\n benchmark_results.json saved")