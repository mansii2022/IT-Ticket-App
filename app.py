import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    model = joblib.load("ticket_classifier.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

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
