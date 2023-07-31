import streamlit as st 
import numpy as np

import pickle

def load_model():
    with open('Pickle\saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
        
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    st.write("### We need some information to predict the salary")
    
    countries = (
        'United Kingdom of Great Britain and Northern Ireland', 
        'Israel',
        'Netherlands',
        'United States of America',
        'Austria',
        'Italy',
        'Canada',
        'Germany',
        'Poland',
        'Norway',
        'France',
        'Sweden',
        'Spain',
        'Belgium',
        'India',
        'Brazil',
        'Switzerland',
        'Denmark',
        'Australia',
        'Portugal',
        'Russian Federation',
        'Turkey'
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )
    
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    #hard to create an empty selectbox

    experience = st.slider("Years of Expeience", 0, 50, 0) #start, end, and default value in the slider
    
    ok = st.button("Predict Salary")
    
    if ok:
        X = np.array([[country, education, experience ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")