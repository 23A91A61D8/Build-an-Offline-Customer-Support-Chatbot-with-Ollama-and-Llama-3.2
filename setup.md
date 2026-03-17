# Setup Guide for Offline Customer Support Chatbot

## 1. Install Ollama

Download and install Ollama from:
https://ollama.com

Verify installation:
ollama --version

---

## 2. Download Llama 3.2 Model

Run the following command:
ollama pull llama3.2:3b

---

## 3. Create Project Directory
mkdir offline-chatbot-project
cd offline-chatbot-project

---

## 4. Create Virtual Environment
python -m venv venv

Activate environment (Git Bash):
source venv/Scripts/activate

---

## 5. Install Dependencies
pip install requests datasets

---

## 6. Project Structure

Ensure your project contains:

- chatbot.py
- README.md
- setup.md
- report.md
- prompts/
- eval/

---

## 7. Run the Chatbot

Make sure Ollama is running, then execute:
python chatbot.py

---

## 8. Output

Results will be saved in:
eval/results.md

---

## 9. Notes

- Ensure Ollama is running before executing the script
- Model responses may take time depending on system performance
- Do not close terminal while script is running