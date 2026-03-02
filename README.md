🎫 IT Ticket Categorization & Validation System

🔗Live App:
👉 https://it-ticket-app-22jkckxlzrvdqb7z2be7sj.streamlit.app/

 Overview

This project is a Machine Learning-based IT Ticket Categorization system that classifies service desk tickets using Natural Language Processing techniques.

The application predicts the ticket category from a short description and displays a confidence score. Low-confidence predictions are flagged for manual review.

The system is fully deployed using Streamlit Cloud for real-time public access.

 Features

TF-IDF based text vectorization

Scikit-learn ML classifier

Real-time prediction via Streamlit UI

Confidence score calculation

Manual review suggestion (< 60% confidence)

Public cloud deployment

🛠 Tech Stack

Python

Scikit-learn

TF-IDF

NumPy

Joblib

Streamlit

📂 Project Structure
IT-Ticket-App/
│
├── app.py
├── ticket_classifier.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── solution.ipynb


🧠 How It Works
<img width="1314" height="560" alt="image" src="https://github.com/user-attachments/assets/c39ee1b5-d37e-4d84-b150-4c281e43bc31" />

User enters ticket description

Text is transformed using TF-IDF

Model predicts ticket category

Confidence score is computed

Low-confidence predictions are flagged for manual validation
<img width="1091" height="560" alt="image" src="https://github.com/user-attachments/assets/87464fb2-a39a-4e58-b27f-1bb47f07fec0" />

 Real-World Application

This system can help automate:

IT Service Desk ticket routing

Incident categorization

Support team workload distribution

Enterprise helpdesk optimization

 Author

Mansi Kumari
Machine Learning & AI Enthusiast

