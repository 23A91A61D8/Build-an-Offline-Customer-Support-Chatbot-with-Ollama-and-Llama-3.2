# Build-an-Offline-Customer-Support-Chatbot-with-Ollama-and-Llama-3.2

## 📌 Project Overview

This project implements an offline customer support chatbot for an e-commerce platform using Ollama and the Llama 3.2 (3B) language model. The chatbot is designed to handle common customer queries such as order tracking, returns, payments, and account issues.

The system runs entirely on a local machine, ensuring **data privacy**, **no API costs**, and **secure processing** of user queries.

---

## 🚀 Key Features

- Offline chatbot using local LLM (Llama 3.2 via Ollama)
- Supports 20 e-commerce customer queries
- Implements **Zero-Shot** and **One-Shot** prompt engineering
- Automated response generation using Python
- Manual evaluation using scoring metrics
- Results logged in a structured markdown table

---

## 🛠️ Technologies Used

- Python
- Ollama
- Llama 3.2 (3B model)
- Requests library
- Hugging Face Datasets (for reference)

---

## 📂 Project Structure
offline-chatbot-project/
│
├── chatbot.py
├── README.md
├── setup.md
├── report.md
│
├── prompts/
│ ├── zero_shot_template.txt
│ └── one_shot_template.txt
│
├── eval/
│ └── results.md


---

## ⚙️ How It Works

1. Loads customer queries
2. Applies Zero-Shot and One-Shot prompt templates
3. Sends request to Ollama API
4. Receives generated response from Llama 3.2
5. Logs responses into `results.md`
6. Performs manual evaluation

---

## 📊 Evaluation Criteria

Each response is evaluated based on:

- Relevance (1–5)
- Coherence (1–5)
- Helpfulness (1–5)

---

## 📈 Key Findings

- Zero-Shot prompting produces more detailed responses
- One-Shot prompting provides better structure and tone
- Both methods have strengths depending on query type
- Local LLMs are effective for basic customer support tasks

---

## 🔐 Advantages of Offline LLM

- No data leaves the system
- Ensures privacy and security
- No dependency on external APIs
- Cost-effective solution

---

## ⚠️ Limitations

- No real-time data access
- Possible incorrect responses (hallucinations)
- Slower performance on CPU
- Limited capability compared to larger models

---

## 🔮 Future Improvements

- Integration with real-time APIs
- Use of larger models (7B/13B)
- Multi-shot prompt engineering
- Web-based user interface

---

## ✅ Conclusion

This project successfully demonstrates the implementation of an offline chatbot using Llama 3.2 and highlights the impact of prompt engineering techniques on model performance.