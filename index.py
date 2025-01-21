
import streamlit as st
import pickle
import numpy as np
import pandas as pd

import joblib

model=pickle.load(open('model.pkl','rb'))


st.title('Credit Card Fraud Detection')
input_val=st.text_input('Enter all required feature values')
input_val=input_val.split(',')

submit=st.button("Submit")

if submit:
    val=np.asarray(input_val,dtype=np.float64)
    pred=model.predict(val)
    if pred==0:
        st.write("Legitimate transaction")
    else:
        st.write("Fraud")