import streamlit as st
import pandas as pd
import numpy as np
from supervised.automl import AutoML
import joblib

model = joblib.load("short_insider2.pkl")

header = st.header("Insider Analysis Model (short)")
feature1 = st.text_input("Enter Feature 1:")
feature2 = st.text_input("Enter Feature 2:")
feature3 = st.text_input("Enter Feature 3:")
feature4 = st.text_input("Enter Feature 4:")

# Convert input to a pandas DataFrame
input_df = pd.DataFrame({
    "Feature 1": [feature1],
    "Feature 2": [feature2],
    "Feature 3": [feature3],
    "Feature 4": [feature4]
})

# Make a prediction using your machine learning model
prediction = model.predict(input_df)

# Display the prediction to the user
st.subheader("Prediction")
st.write(prediction)