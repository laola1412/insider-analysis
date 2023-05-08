import streamlit as st
import pandas as pd
import numpy as np
from supervised.automl import AutoML
import joblib
import os
from supervised.automl import AutoML

# main_script_path = os.path.join("..", "c:", "Users", "Nils", "Desktop", "insider_ml", "init.py")

header = st.header("Insider Analysis Model")
model_explanation = st.write("The model predicts, whether a certain company with recent insider trades will outperform the market. If you choose the 'long' model and  the prediction returns 1, the company has a high probability of significant outperformance. If you choose the 'short' model and the prediction returns 1, the company is likely to underperform heavily.")

selected_model = st.selectbox("Pick the long or short model", ["Long", "Short"])

if selected_model == "Long":
    st.image("final_model/Ensemble/confusion_matrix.png", width=500)
    model = joblib.load("final_long_model.pkl")
else:
    st.image("final_model_short/Ensemble/confusion_matrix.png", width=500)
    model = joblib.load("final_short_model.pkl")

selected_input = st.selectbox("Do you want to input your data by hand or with a .csv?", ["Input", "CSV"])

if selected_input == "CSV":
    csv_input = st.file_uploader("Upload your .csv file", type=["csv"])
    df = pd.read_csv(csv_input, encoding="utf-8", sep=";")
    original_df = df.copy()
    
else:
    feature1 = st.number_input("Enter Feature 1:")
    feature2 = st.number_input("Enter Feature 2:")
    feature3 = st.number_input("Enter Feature 3:")
    feature4 = st.number_input("Enter Feature 4:")
    
# format raw csv data to model-ready dataframe
df.drop(["Industry", "Filing Date", "date 1y before", " unratechange ", "better date before", "firstofmonth", "date 1y after", "date 1y after better", "Period", "Quarter", "ticker", "Company Name", "1y before price", "target", " 1yafterpricechange "], axis=1, inplace=True)
df = df.astype(str)
df =  df.apply(lambda x: x.str.replace(",",".").str.replace("%","").str.replace("$",""))
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.apply(lambda x: x.str.replace(r'(\d+)\.(\d+)\.', r'\1.\2').str.replace(',', ''))

for col in df.columns:
    try:
        df[col] = df[col].astype(float)
    except ValueError:
        # replace non-numeric values with NaN
        df[col] = df[col].replace('-', pd.NaT)
        
        
# df["target"] = df["target"].apply(lambda x: 1 if x < -50 else 0)

# show table
st.write(df) 

# run the model
# X = df.drop("target", axis=1)
# y = df["target"]

st.header("Prediction")
outcome = model.predict(df)

# add company name and rename output column
result = pd.DataFrame({'Company Name': original_df['Company Name'], 'Prediction': outcome}).rename(columns={0: 'Prediction'})
result = result.set_index('Company Name')

st.write(result)
st.balloons()


    
# balloon1 = st.balloons()

# # Convert input to a pandas DataFrame
# input_df = pd.DataFrame({
#     "Feature 1": [feature1],
#     "Feature 2": [feature2],
#     "Feature 3": [feature3],
#     "Feature 4": [feature4]
# })

# # Make a prediction using your machine learning model
# prediction = model.predict(input_df)

# # Display the prediction to the user
# st.subheader("Prediction")
# st.write(prediction)