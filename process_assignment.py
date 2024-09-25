#!/usr/bin/env python3

import requests
import os
import json

def send_to_ollama(data):
    url = "http://molly-server.university.edu/ollama-model"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def main():
    # Assuming all files are in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    data = {}
    for file in files:
        with open(file, 'r') as f:
            data[file] = f.read()

    # Send data to Ollama model
    model_response = send_to_ollama(data)

    # Write model response to feedback.md
    with open('feedback.md', 'w') as f:
        f.write("# Model Feedback\n\n")
        f.write(model_response.get('feedback', 'No feedback received.'))

if __name__ == "__main__":
    main()
