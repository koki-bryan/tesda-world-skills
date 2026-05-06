import json, os, requests

def safeDivide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide a number to zero"
    
print(safeDivide(1,0))

allowed_ch="0123456789+-()*/**%."
def safeCalculate(expr):
    for ch in expr:
        if(ch not in allowed_ch):
            return "Invalid Expression"
    return eval(expr, {"__builtins__": None})

print(safeCalculate("3.2-9_8"))
#using requests
payload={
    "model":"mistral",
    "prompt": "i have allergic rhinitis what are the top recommended prescription drugs by the best allegologists",
    "stream": False
}
ollama_api="http://localhost:11434/api/generate"
r=requests.post(ollama_api, json=payload)
data=r.json()
print(data['response'])

