from flask import Flask, render_template, request, jsonify
import requests

app= Flask(__name__, template_folder='templates')

OLLAMA_URL = "http://ollama:11434/api/chat"

@app.route('/')
def index_route():
    return render_template('index.html')

conversation_history=[]

@app.route('/api/chat', methods=["POST"])
def generate_response():
    data=request.get_json()
    
    user_message = data.get('prompt')
    
    if not user_message:
        return {'error': 'No prompt attached'}
    
    conversation_history.append({"role": "user", "content": user_message})
    try:
        payload={
            "model": "mistral", 
            "messages": conversation_history,
            "stream": False
        }
        
        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status()
        response = r.json()
        
        ai_response=(response.get('message').get('content'))
        conversation_history.append({'role':'assistant', 'content': ai_response})
        print(conversation_history)
        return jsonify({"response": ai_response})
    except Exception as e:
        conversation_history.pop()
        return jsonify({'error': str(e)}), 500

app.run(host='0.0.0.0',port=5000, debug=True)