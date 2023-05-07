import pandas as pd
import numpy as np
import streamlit as st

pd.set_option('display.max_columns', None)

df = pd.read_csv("insider_book.csv",  encoding="utf-8", sep=";")
df.drop(["Industry", "Filing Date", "date 1y before", " unratechange ", "better date before", "firstofmonth", "date 1y after", "date 1y after better", "Period", "Quarter", "ticker", "Company Name", "1y before price", " 1yafterpricechange "], axis=1, inplace=True)

df = df.astype(str)
df=  df.apply(lambda x: x.str.replace(",",".").str.replace("%","").str.replace("$",""))

import numpy as np
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df = df.apply(lambda x: x.str.replace(r'(\d+)\.(\d+)\.', r'\1.\2').str.replace(',', ''))

# convert columns to float
for col in df.columns:
    try:
        df[col] = df[col].astype(float)
    except ValueError:
        # replace non-numeric values with NaN
        df[col] = df[col].replace('-', pd.NaT)
        
# change target feature to binary (1 if > 20 , 0 if <= 2)
df["target"] = df["target"].apply(lambda x: 1 if x < -50 else 0)


from supervised.automl import AutoML
from sklearn.metrics import log_loss

X = df.drop("target", axis=1)
y = df["target"]

automl = AutoML(eval_metric="average_precision", results_path = "previous_autoML")
automl.fit(X, y)

st.write("Model trained")