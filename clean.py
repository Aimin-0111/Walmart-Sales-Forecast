# ================================= Intialization  ================================
import requests

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

!pip install -q gdown
import gdown

url = "https://drive.google.com/uc?id=1u37-Uh9xNIE8UCMiPq8iNHCBqyiagVR3"
gdown.download(url, "data.csv", quiet=False)
df = pd.read_csv("data.csv")

# Make copy of data file
df_copy = df.copy()
# Output data table
df_copy
# Find all unique values in temperature column
df_copy['Temperature'].unique()
# Show first 5 values
df_copy["Temperature"].head()
#- Object data type means mixed data types
# Check null values
df_copy[df_copy["Temperature"].str.contains("\?")].shape[0]
#- No null values
# One more check
df_copy["Temperature"].isnull().sum().sum()

def Markdowns_fixer(df,Markdown_name):
    def unit_fixer(original): #defining a function to fix the unit of the Fuel_Price column
        split_arr = str(original).split(" ")
        if len(split_arr) > 1 and split_arr[0] == "CAD":
            return float(split_arr[1])
        else:
            return float(split_arr[0])
    #print(f"Before imputation, {Markdown_name} has: {df[Markdown_name].isnull().sum()}")
    print("\n") 
    df[Markdown_name] = df[Markdown_name].apply(lambda x: unit_fixer(x))
    #df[Markdown_name] = df[Markdown_name].apply(lambda x: type(x)) Testing the type of the Markdown_name column after applying the unit_fixer function
    median_markdown = df[Markdown_name].median() # calculating the median
    df[Markdown_name] = df[Markdown_name].fillna(median_markdown) # replacing missing values without chained inplace assignment
    #print(f"After imputation, {Markdown_name} has: {df[Markdown_name].isnull().sum()}")
    return df


def IsHoliday_Fixing(df):
  dic = {'no' : 'FALSE',
        'YES' : 'TRUE',
        'yes' : 'TRUE',
        'NO' : 'FALSE', 
        'FAL' : 'FALSE', 
        'T' : 'TRUE',
        'F' : 'FALSE', 
        '1' : 'TRUE', 
        '0' : 'TRUE'}
  df['IsHoliday'] = df['IsHoliday'].apply(lambda x: dic.get(x,x))
  df['IsHoliday'] = df['IsHoliday'].astype(bool)
  return(df)

def Unemployment_Fixing(df_copy):

  df_copy = df.copy()

  median_unemployment = df_copy["Unemployment"].median()
  df_copy["Unemployment"].fillna(median_unemployment, inplace=True)
  df_copy.isnull().sum()
  df['Unemployment'] = df['Unemployment'].round(2)
  return df_copy
  
def Fuel_Price_Fixing(df): #Fxing the Fuel_Price column to remove the currency unit and convert it to float
    
    def unit_fixer(original): #defining a function to fix the unit of the Fuel_Price column
        split_arr = str(original).split(" ")
        if len(split_arr) > 1 and split_arr[0] == "CAD":
            return float(split_arr[1])
        else:
            return float(split_arr[0])
        
    df['Fuel_Price'] = df['Fuel_Price'].apply(lambda x: unit_fixer(x))
    '''df['Fuel_Price'] = df['Fuel_Price'].apply(lambda x: type(x))''' #Testing the type of the Fuel_Price column after applying the unit_fixer function
    median_fuel_price = df['Fuel_Price'].median() # calculating the median
    df['Fuel_Price'] = df['Fuel_Price'].fillna(median_fuel_price) # replacing missing values without chained inplace assignment
    return df
  
def DataTesting():
  



# ================================= Temperature  ================================


def fix_temperature(temperatures):

    # Convert to string and clean up extra whitespace
    temperatures_str = str(temperatures).strip()
    
    # Remove extra trailing 'C's 
    temperatures_str = temperatures_str.rstrip("C").strip()
    
    # Re-append a single 'C' standard suffix
    return f"{float(temperatures_str):.2f} °C"

# Assign temperature fix back to data file
df_copy["Temperature"] = df_copy['Temperature'].astype(str).apply(fix_temperature)

df_copy["Temperature"].head()


def main():
    df_cleaned = df_copy.copy()
    return df_cleaned
