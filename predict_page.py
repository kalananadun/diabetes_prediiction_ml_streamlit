import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import pickle
# ['age', 'hypertension', 'bmi', 'HbA1c_level', 'blood_glucose_level',
#       'gender_Female', 'gender_Male']


def load_model():
    with open('logistic_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model()

rfc = data["model"]
label_encoder = data["label_encoder"]

def show_predict():
    data = load_model()

    rfc = data["model"]
    label_encoder = data["label_encoder"]
    
    st.title("Diabetes Prediction Application")
    st.write("Fill the correct informations in the fields")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your Age",min_value=0, max_value=100)
    hypertenstion = st.number_input("Enter the Hypertension level")
    HbA1c_level = st.number_input("Enter the HbA1c level ")
    blood_glucose_level = st.number_input("Enter the glucose level ")
    bmi = st.number_input("Enter the BMI?",min_value=0)
    options = ["Male", "Female"]
    gender = st.radio("Select your status:", options)
    
    ok = st.button("Submit")
    if ok:
        
        #['age', 'hypertension', 'bmi', 'HbA1c_level', 'blood_glucose_level',
        #'gender_Female', 'gender_Male']
        if gender == 'Male':
           gender_Female=0
           gender_Male=1 
           
        if gender == 'Female':
           gender_Female=1
           gender_Male=0 
        
        X= pd.DataFrame({
            'age':age,
            'hypertension':[hypertenstion],
            'bmi':[bmi],
            'HbA1c_level':[HbA1c_level],
            'blood_glucose_level':[blood_glucose_level],
            'gender_Female':[gender_Female],
            'gender_Male': [gender_Male]
            
        })
        
        predict = rfc.predict(X)
        
        if  predict==1:
            # this person has diabetes 
            message = name + " " + "Unfortunately you have diabetes"
        else:
            message = name + " " + "Fortunately you don't have diabetes"
        st.write(message)

    
    
     


