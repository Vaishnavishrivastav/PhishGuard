import streamlit as st
import pickle
import requests
import numpy as np

# --- Load the model from GitHub ---
MODEL_URL = "https://raw.githubusercontent.com/Vaishnavishrivastav/PhishGuard/main/phishguard_model.pkl"

@st.cache_resource
def load_model():
    response = requests.get(MODEL_URL)
    response.raise_for_status()  # Raises error if download fails
    model = pickle.loads(response.content)
    return model

model = load_model()

# --- Streamlit App UI ---
st.title("🛡️ PhishGuard - URL Phishing Detection App")
st.write("Detect whether a URL is **legitimate or phishing** using a trained ML model.")

# --- User input ---
url_features = st.text_input("Enter URL features (comma-separated if manual input):")

if st.button("Check URL"):
    try:
        # Here, you would extract real features — for now, let’s simulate numeric input
        features = np.array([float(x.strip()) for x in url_features.split(",")]).reshape(1, -1)
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("⚠️ This URL is likely a **Phishing Website!**")
        else:
            st.success("✅ This URL seems **Legitimate**.")
    except Exception as e:
        st.warning(f"Error: {e}")
        st.info("Make sure you enter valid numeric features for testing.")
