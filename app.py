import streamlit as st
import pickle
import pandas as pd
import os
st.set_page_config(
    page_title="Starbucks Calories Predictor",
    page_icon="☕"
)

st.title("☕ Starbucks Calories Predictor")
st.write("Predict the calories in your Starbucks drink.")

@st.cache_resource
@st.cache_resource
def load_model():
    model_path = os.path.join(
        os.path.dirname(_file_),
        "starbucks_decision_model_v1 (1).pkl"
    )
    with open(model_path, "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
    st.success("Model loaded successfully!")

    st.info(
        "Model is ready. We need the original input "
        "features and their order to make predictions."
    )

except Exception as e:
    st.error(f"Could not load model: {e}")
