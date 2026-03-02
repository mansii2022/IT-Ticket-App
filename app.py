import streamlit as st
import pickle
import numpy as np

# Load trained model and vectorizer
model = pickle.load(open("ticket_classifier.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

st.set_page_config(page_title="IT Ticket Validation", layout="centered")

st.title("🎫 IT Ticket Categorization & Validation System")

st.write("Enter a ticket short description to validate its category.")

user_input = st.text_area("Ticket Description")

if st.button("Validate Ticket"):
    if user_input.strip() != "":
        text_vec = vectorizer.transform([user_input])
        prediction = model.predict(text_vec)[0]
        confidence = np.max(model.predict_proba(text_vec))

        st.subheader("Prediction Result")
        st.write("**Predicted Category:**", prediction)
        st.write("**Confidence Score:**", round(confidence, 2))

        if confidence < 0.60:
            st.warning("⚠ Low Confidence – Manual Review Suggested")
        else:
            st.success("✔ Classification Looks Confident")
    else:
        st.error("Please enter a ticket description.")