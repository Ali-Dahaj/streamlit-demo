# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:28:19 2023

@author: AliDahaj
"""
import streamlit as st
import pandas as pd
#%%
file_path = 'C:/Users/AliDahaj/Documents/python_scripts/cars.xlsx'
FILE_PATH = 'C:/Users/AliDahaj/Documents/python_scripts/cars.xlsx'

def is_car_duplicate(color, model, year):
    df = pd.read_excel(FILE_PATH, index_col= 'car num')
    is_duplicate = df[(df["Color"].str.lower() == color.lower()) &
                      (df["Model"].str.lower() == model.lower()) &
                      (df["Year"] == year)].shape[0] > 0
    return is_duplicate

# Define function to add a new car to the Excel file
def add_car(color, model, year):
    df = pd.read_excel(FILE_PATH, index_col = 'car num')
    max_car_number = df.shape[0]
    new_car_number = max_car_number + 1
    df.loc[new_car_number] = [color, model, year]
    df.to_excel(FILE_PATH, index = True)
    st.success(f"New car with car number {new_car_number} has been added to the file.")

# Define the Streamlit app
def main():
    # Set page title
    st.set_page_config(page_title="Add Car")

    # Add page title
    st.title("Add Car")

    # Add form for user to input car information
    color = st.selectbox('Select car color:', ['Red', 'Blue', 'Green', 'Yellow'])
    model = st.text_input("Enter the car model", value="SUV")
    year = st.number_input("Enter the car year", value=2021, min_value=1900, max_value=2100)

    # Add button to submit the form
    if st.button("Add"):
        # Check if the car already exists in the Excel file
        if is_car_duplicate(color, model, year):
            st.warning("This car already exists in the file.")
        else:
            add_car(color, model, year)
    st.dataframe(pd.read_excel(FILE_PATH, index_col = 'car num'), 300, 300)

if __name__ == "__main__":
    main()

