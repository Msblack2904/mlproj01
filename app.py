import pickle
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



pickle_in = open("bhp.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "welcome all"


def property_eval(location,sqft,bath,bhk):
    prediction = classifier.predict([[location,sqft,bath,bhk]])
    print(prediction)
    return prediction


def main():
    st.title("Bangalore property price prediction")
    location= st.text_input("Location" )
    sqft = st.number_input("Area in square fit",min_value=1000)
    bath = st.number_input("Number of bathrooms",min_value=1,step=1)
    bhk = st.number_input("BHK",min_value=1,step=1)
    result=""
    if st.button("Predict"):
        result=property_eval(location,sqft,bath,bhk)
    st.success('The output is {}'.format(result))
   

if __name__=='__main__':
    main()
    