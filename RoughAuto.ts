import * as readline from "readline";
import fetch from 'node-fetch';
import { ReadableStream } from 'node:stream/web'; // Import the ReadableStream type

const model = "llama 2";

type Message = {
    role: "assistant" | "user" | "system";
    content: string;
};

const messages: Message[] = [{
    role: "system",
    content: "you are a helpful AI agent."
}];

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

async function chat(messages: Message[]): Promise<Message> {
    const body = {
        model: model,
        messages: messages
    };

    const response = await fetch("http://localhost:11434/api/chat", {
        method: "POST",
        body: JSON.stringify(body),
        headers: { 'Content-Type': 'application/json' }
    });

    const reader = (response.body as unknown as ReadableStream<Uint8Array>)?.getReader(); // Cast response.body to unknown first, then to ReadableStream<Uint8Array>
    if (!reader) {
        throw new Error("Failed to read response body");
    }

    let content = "";
    while (true) {
        const { done, value } = await reader.read();
        if (done) {
            break;
        }
        const rawJson = new TextDecoder().decode(value);
        const json = JSON.parse(rawJson);
        if (json.done === false) {
            process.stdout.write(json.message.content);
            content += json.message.content;
        }
    }

    return { role: "assistant", content: content };
}

async function askQuestion(): Promise<void> {
    return new Promise<void>((resolve) => {
        rl.question("\n\nAsk a question: (press enter alone to quit)\n\n", async (userInput) => {
            if (userInput.trim() === "") {
                rl.close();
                console.log("Thank you. Goodbye.\n");
                console.log("=======\nHere is the message history that was used in this conversation \n=======\n");
                messages.forEach(message => {
                    console.log(message);
                });
                resolve();
            } else {
                console.log();
                messages.push({ role: "user", content: userInput });
                messages.push(await chat(messages));
                await askQuestion(); // ask the next question
            }
        });
    });
}

async function main() {
    await askQuestion();
}

main();