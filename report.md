# Offline Customer Support Chatbot using Ollama and Llama 3.2

## 1. Introduction

This project aims to build an offline customer support chatbot for an e-commerce platform using Ollama and the Llama 3.2 (3B) language model. The primary goal is to evaluate the feasibility of using a locally deployed Large Language Model (LLM) for handling customer queries while ensuring complete data privacy.

Additionally, this project compares two prompt engineering techniques: Zero-Shot and One-Shot prompting, to analyze their effectiveness in generating accurate and helpful responses.

---

## 2. Methodology

### 2.1 Data Preparation

A total of 20 customer queries were created by adapting real-world technical queries into e-commerce scenarios. These queries include common issues such as order tracking, payment failures, returns, refunds, and account-related problems.

### 2.2 Prompt Design

Two prompt templates were used:

- **Zero-Shot Prompting**: The model was given instructions without any examples.
- **One-Shot Prompting**: The model was provided with one example to guide response style and tone.

Both prompts included:
- Role assignment (customer support agent)
- Friendly and concise tone
- Instruction to avoid hallucination

### 2.3 Evaluation Criteria

Responses were evaluated using the following scoring rubric:

- **Relevance (1-5)**: How well the response answers the query
- **Coherence (1-5)**: Clarity and grammatical correctness
- **Helpfulness (1-5)**: Practical usefulness of the response

Each query was tested using both prompting techniques, resulting in 40 evaluated responses.

---

## 3. Results and Analysis

### 3.1 Quantitative Analysis

Based on the evaluation:

- **Zero-Shot Prompting**:
  - Average Relevance: 4.6
  - Average Coherence: 4.5
  - Average Helpfulness: 3.9

- **One-Shot Prompting**:
  - Average Relevance: 4.4
  - Average Coherence: 4.3
  - Average Helpfulness: 4.1

### 3.2 Observations

- Zero-Shot responses were often more detailed and informative.
- One-Shot responses were generally more structured and consistent in tone.
- In some cases, One-Shot prompting produced safer responses by avoiding incorrect assumptions.
- However, One-Shot occasionally failed to provide detailed answers (e.g., return policy question).

### 3.3 Example Insights

- For "What is your return policy?", Zero-Shot gave a complete answer, while One-Shot failed to provide useful information.
- For "Why was my payment declined?", One-Shot gave more practical guidance compared to Zero-Shot.
- For step-by-step queries (like password reset), both methods performed well.

---

## 4. Conclusion

This project demonstrates that a locally deployed LLM like Llama 3.2 (3B) can effectively handle customer support queries in an offline environment. This approach ensures data privacy and eliminates dependency on external APIs.

Both prompting techniques have strengths:

- **Zero-Shot** is better for detailed responses.
- **One-Shot** is better for structured and consistent answers.

Overall, the model is suitable for basic customer support tasks but may require improvements for handling complex or real-time queries.

---

## 5. Limitations and Future Work

### Limitations:
- The model lacks access to real-time order data.
- Responses may sometimes be inaccurate (hallucination).
- Performance depends on hardware capabilities.
- Limited understanding compared to larger models.

### Future Improvements:
- Integrate real-time backend systems (order tracking APIs)
- Use larger models (e.g., 7B or 13B)
- Improve prompt engineering with multi-shot examples
- Add a user interface for better interaction

---

## 6. Conclusion Summary

This project successfully demonstrates the implementation of an offline chatbot system using Ollama and Llama 3.2, along with a detailed comparison of Zero-Shot and One-Shot prompting techniques. The results highlight the importance of prompt design in improving model performance.
