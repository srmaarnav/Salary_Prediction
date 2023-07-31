import streamlit as st


st.set_page_config(
        page_title="Salary Prediction",
)

from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
    
elif page == "Explore":
    show_explore_page()