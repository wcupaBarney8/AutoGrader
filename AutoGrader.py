import requests
import json

model = "llama 2"

messages = [{
    "role": "system",
    "content": "you are a helpful AI agent."
}]

def chat(messages):
    body = {
        "model": model,
        "messages": messages
    }

    response = requests.post("http://localhost:11434/api/chat", json=body)
    response.raise_for_status()

    content = ""
    for chunk in response.iter_content(chunk_size=None):
        raw_json = chunk.decode('utf-8')
        json_data = json.loads(raw_json)
        if not json_data.get("done", True):
            print(json_data["message"]["content"], end="")
            content += json_data["message"]["content"]

    return {"role": "assistant", "content": content}

def ask_question():
    while True:
        user_input = input("\n\nAsk a question: (press enter alone to quit)\n\n")
        if user_input.strip() == "":
            print("Thank you. Goodbye.\n")
            print("=======\nHere is the message history that was used in this conversation \n=======\n")
            for message in messages:
                print(message)
            break
        else:
            print()
            messages.append({"role": "user", "content": user_input})
            messages.append(chat(messages))

if __name__ == "__main__":
    ask_question()