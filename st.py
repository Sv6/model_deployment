import streamlit as st
import joblib

st.title('Hello World')
model = joblib.load('linear.pkl')

st.write('## Salary Prediction')

X = st.slider('Experience', 0, 40)
y = model.predict([[X]])
st.write('Salary is: ', y)
# streamlit run filename.py << in terminal