# ================================= Intialization  ================================
import requests

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


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

#===================================== Holiday =====================================

def IsHoliday_Fixing(df):
  dic = {'no' : 'FALSE',
        'YES' : 'TRUE',
        'yes' : 'TRUE',
        'NO' : 'FALSE', 
        'FAL' : 'FALSE', 
        'T' : 'TRUE',
        'F' : 'FALSE', 
        '1' : 'TRUE', 
        '0' : 'FALSE'}
  df['IsHoliday'] = df['IsHoliday'].apply(lambda x: dic.get(x,x))
  df['IsHoliday'] = df['IsHoliday'].astype(bool)
  return(df)

def Unemployment_Fixing(df_copy):

  median_unemployment = df_copy["Unemployment"].median()
  df_copy["Unemployment"] = df_copy["Unemployment"].fillna(median_unemployment)
  df_copy.isnull().sum()
  df_copy['Unemployment'] = df_copy['Unemployment'].round(2)
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
    print()
    
# ================================= Temperature  ================================


def fix_temperature(temperatures):

    # Convert to string and clean up extra whitespace
    temperatures_str = str(temperatures).strip()
    
    # Remove extra trailing 'C's 
    temperatures_str = temperatures_str.rstrip("C").strip()
    
    # Re-append a single 'C' standard suffix
    #return f"{float(temperatures_str):.2f} °F"
    return float(f"{float(temperatures_str):.2f}")

# Assign temperature fix back to data file
df_copy["Temperature"] = df_copy['Temperature'].astype(str).apply(fix_temperature)

# ======================================== CPI =======================================

# Check null values

df_copy["CPI"].isnull().sum().sum()

# Check unique values
df_copy["CPI"].unique()

# Check data types
df_copy['CPI'].apply(lambda x: type(x))

#- All data is float

# Perform unconditional imputation using median

# First check where null values are
df_copy[df_copy['CPI'].isnull()]

# Calculate 
median_CPI = df_copy['CPI'].median() # calculating the median
df_copy["CPI"] = df_copy['CPI'].fillna(median_CPI) # replacing missing values, (inplace = True) replaces values in the dataframe

# Check now
print(df_copy[df_copy['CPI'].isnull()])

# Count null values/see nulls values in CPI column
df_copy.isnull().sum()

# Print CPI column
df_copy["CPI"]

def fix_CPI(CPIs):
    
    # Change decimal places
    return float(f"{CPIs:.3f}")

# Assign temperature fix back to data file
df_copy["CPI"] = df_copy['CPI'].apply(fix_CPI)

#================================ Markdowns ==============================

def Markdowns_fixer(df,Markdown_name):

    markdowns_mapper = {
      "NA": np.nan, # NA
      "NAA": np.nan, # NAA
      "nan": np.nan,  # nan
      "NNA": np.nan,
      "na": np.nan,
      "N/A": np.nan,
      }
    
    df_copy[Markdown_name] = df_copy[Markdown_name].apply(lambda x: markdowns_mapper.get(x, x))

    def unit_fixer(original): #defining a function to fix the unit of the Markdowns column
        split_arr = str(original).split(" ")
        if len(split_arr) > 1 and split_arr[0] == "CAD":
            return float(split_arr[1])
        else:
            return float(split_arr[0])

    #df.loc[df[Markdown_name].str.contains("NA"), Markdown_name] = np.nan  

    #df.loc[df[Markdown_name].str.contains("NAA"), Markdown_name] = np.nan  

    #df.loc[df[Markdown_name].str.contains("NAA"), Markdown_name] = np.nan

    #print(f"Before imputation, {Markdown_name} has: {df[Markdown_name].isnull().sum()}")
    print("\n") 
    df[Markdown_name] = df[Markdown_name].apply(lambda x: unit_fixer(x))
    #df[Markdown_name] = df[Markdown_name].apply(lambda x: type(x)) Testing the type of the Markdown_name column after applying the unit_fixer function
    '''median_markdown = df[Markdown_name].median() # calculating the median
    df[Markdown_name] = df[Markdown_name].fillna(median_markdown) # replacing missing values without chained inplace assignment
'''    #print(f"After imputation, {Markdown_name} has: {df[Markdown_name].isnull().sum()}")
    return df

def main(df_copy):
    
    df_copy = Markdowns_fixer(df_copy,"MarkDown1")
    df_copy = Markdowns_fixer(df_copy,"MarkDown2")
    df_copy = Markdowns_fixer(df_copy,"MarkDown3")
    df_copy = Markdowns_fixer(df_copy,"MarkDown4")
    df_copy = Markdowns_fixer(df_copy,"MarkDown5")
    df_copy = IsHoliday_Fixing(df_copy)
    df_copy = Unemployment_Fixing(df_copy)
    df_copy = Fuel_Price_Fixing(df_copy)
    
    
    df_cleaned = df_copy.copy()
    return df_cleaned
df_cleaned = main(df_copy)


df_copy

# ====================================== Visualization ========================================

# ============= Scatter Plot ==============



# numeric columns only — Date and IsHoliday aren't histogram material
cols = [
    'Temperature',
    'Fuel_Price',
    'MarkDown1',
    'MarkDown2',
    'MarkDown3',
    'MarkDown4',
    'MarkDown5',
    'Unemployment',
]
fig, axes = plt.subplots(3, 3, figsize=(15, 10))
axes = axes.flatten()


for i, col in enumerate(cols): #Create a scatter plot for each variable

    x = df_cleaned[col]
    sc = axes[i].scatter(x, df_cleaned['CPI'], c=df_cleaned['Store'],
                         cmap='tab20', s=5, alpha=0.5)
    lo, hi = x.quantile([0.01, 0.98])
    pad = (hi - lo) * 0.05
    axes[i].set_xlim(lo - pad, hi + pad)
    axes[i].set_xlabel(col)      # variable on x
    axes[i].set_ylabel('CPI')    # CPI on y
    axes[i].set_title(f'CPI vs {col}')

for j in range(len(cols), len(axes)):
    axes[j].axis('off')          # hide the leftover 9th panel

cax = axes[8].inset_axes([0.35, 0.05, 0.08, 0.9])   # [x, y, width, height] in panel coords
fig.colorbar(sc, cax=cax, label='Store')

plt.tight_layout()
plt.show()

df_copy['Temperature']
