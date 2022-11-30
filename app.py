import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Division on Streamlit and Heroku

""")
#Get Input

st.header('User Input Parameters')


divident = st.number_input("Dividend")
divisor = st.number_input("Divisor")

quotient = divident/divisor if divisor != 0 else "Error" 
st.write()

