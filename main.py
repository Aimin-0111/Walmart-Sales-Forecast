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

def Fuel_Price_Fixing(df): #Fxing the Fuel_Price column to remove the currency unit and convert it to float
    def unit_fixer(original): #defining a function to fix the unit of the Fuel_Price column
        split_arr = str(original).split(" ")
        if len(split_arr) > 1 and split_arr[0] == "CAD":
            return float(split_arr[1])
        else:
            return float(split_arr[0])
        
    df['Fuel_Price'] = df['Fuel_Price'].apply(lambda x: unit_fixer(x))
    '''df['Fuel_Price'] = df['Fuel_Price'].apply(lambda x: type(x))''' #Testing the type of the Fuel_Price column after applying the unit_fixer function
    return df
  
def DataTesting():
  

def main():
  return 0
