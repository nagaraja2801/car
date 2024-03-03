import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('D:\PYTHON\Machine Learning\Diabetes_Prediction\Real\pipe.pkl','rb'))
data = pickle.load(open('D:\PYTHON\Machine Learning\Diabetes_Prediction\Real\df.pkl','rb'))

st.title("Diabetes Predictor")

#name 
name =int(st.number_input("name",min_value = 0,step = 1))

#company
Pregnancy_count = int(st.number_input("company",min_value = 0,step = 1))

#year
year = int(st.number_input("year",min_value = 0,step = 1))

#price = int(st.number_input("price",min_value = 0,step = 1))

#kms_driven
kms_drive = int(st.number_input("Skin Thickness",min_value = 0,step = 1))

#fueal_type
fueal type = int(st.number_input("fueal_type",min_value = 0,step = 1))

#BMI
bmi = st.number_input("BMI",min_value = 0)

#DiabetesPedigree
Dp = st.number_input("DiabetesPedigree",min_value = 0)

if st.button("Predict"):
    query = np.array([Pregnancy_count,Glucose,BP,skin,insulin,bmi,Dp,Age])
    query = query.reshape(1,8)
    result = float(pipe.predict(query))
    if(result >= 0.50):
        st.title("You are Diabetic")
    else:
        st.title("You are not Diabetic")
    