from flask import Flask, render_template, request, jsonify
import requests

app= Flask(__name__, template_folder='templates')

OLLAMA_URL = "http://ollama:11434/api/chat"

@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/email')
def email_route():
    return render_template('email.html')