import requests
import json

# API Configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Load prompt templates
def load_template(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Query Ollama API
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "Error: Unable to fetch response"

# 20 Customer Queries
queries = [
    "How can I track my order?",
    "My discount code is not working at checkout.",
    "What is your return policy?",
    "How long does shipping take?",
    "Can I cancel my order after placing it?",
    "I received a damaged product. What should I do?",
    "Do you offer cash on delivery?",
    "How can I change my delivery address?",
    "Why was my payment declined?",
    "Can I exchange an item instead of returning it?",
    "How do I contact customer support?",
    "Do you provide international shipping?",
    "How can I apply a coupon code?",
    "What should I do if I received the wrong item?",
    "How do I reset my account password?",
    "Can I order without creating an account?",
    "How do I check my order history?",
    "Are there any additional delivery charges?",
    "What payment methods do you accept?",
    "How can I get a refund for my order?"
]

def main():
    # Load templates
    zero_shot_template = load_template("prompts/zero_shot_template.txt")
    one_shot_template = load_template("prompts/one_shot_template.txt")

    # Open results file
    with open("eval/results.md", "w", encoding="utf-8") as file:
        
        # Write table header
        file.write("| Query # | Customer Query | Prompt Type | Response | Relevance | Coherence | Helpfulness |\n")
        file.write("|---------|----------------|-------------|----------|------------|------------|--------------|\n")

        # Loop through queries
        for i, query in enumerate(queries, start=1):

            # Zero-shot
            zero_prompt = zero_shot_template.replace("{query}", query)
            zero_response = query_ollama(zero_prompt)

            file.write(f"| {i} | {query} | Zero-Shot | {zero_response} |  |  |  |\n")

            # One-shot
            one_prompt = one_shot_template.replace("{query}", query)
            one_response = query_ollama(one_prompt)

            file.write(f"| {i} | {query} | One-Shot | {one_response} |  |  |  |\n")

            print(f"Completed Query {i}")

if __name__ == "__main__":
    main()