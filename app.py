import streamlit as st

st.write("""
# Division on Streamlit and Heroku

""")
#Get Input

st.header('User Input Parameters')


divident = st.number_input("Dividend")
divisor = st.number_input("Divisor")

quotient = divident/divisor if divisor != 0 else "Error" 

st.write("Quotient:"+quotient)
