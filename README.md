Project Overview
This project was developed during my internship with the AICTE Edunet Foundation. The goal was to solve a common problem for students: the struggle to understand complex academic concepts without immediate access to a teacher.

This "Study Buddy" is a web-based tool that uses Large Language Models (LLMs) to simplify topics, summarize long study notes, and generate quick quizzes for self-assessment.

Core Features
Concept Explainer: Breaks down difficult topics (like Quantum Physics or Data Structures) into simple, student-friendly language.

Note Summarizer: Converts long paragraphs into concise, readable bullet points.

Quiz Generator: Creates instant Multiple Choice Questions (MCQs) to help students test their knowledge after studying.

Tech Stack
Frontend: Streamlit (Python-based web framework)

AI Backend: Hugging Face Inference API

Model: Llama-3.2-3B-Instruct (via Meta)

Environment: Python 3.x, VS Code

Project Structure
Plaintext
AI-STUDY-BUDDY/
├── app.py              # Main application logic and UI
├── .env                # API keys (not shared in public repo)
├── requirements.txt    # Required Python libraries
└── README.md           # Documentation
How to Run This Project
Clone the folder and open it in VS Code.

Install dependencies:

Bash
pip install -r requirements.txt
Setup your API Key:

Create a .env file in the root directory.

Add your token: HF_TOKEN=your_huggingface_token_here

Launch the app:

Bash
streamlit run app.py
Access the tool at http://localhost:8501 in your browser.

Author
Ankit Kumar Tiwari
BCA 2026