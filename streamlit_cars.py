# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:28:19 2023

@author: AliDahaj
"""
import streamlit as st
import pandas as pd

def add_car_to_excel(color, size, model):
    # Read the Excel file
    df = pd.read_excel('cars.xlsx')
    
    # Check if there is already a car with the same properties
    if ((df['Color'] == color) & (df['Size'] == size) & (df['Model'] == model)).any():
        st.warning("A car with these properties already exists in the Excel file.")
    else:
        # Add the car to the Excel file
        new_car = {'Color': color, 'Size': size, 'Model': model}
        df = df.append(new_car, ignore_index=True)
        df.to_excel('cars.xlsx', index=False)
        st.success("Car added to the Excel file!")

# Set up the Streamlit app
st.title("Car Adder")

color = st.text_input("Enter the color of the car:")
size = st.text_input("Enter the size of the car:")
model = st.text_input("Enter the model of the car:")

if st.button("Add Car"):
    add_car_to_excel(color, size, model)

