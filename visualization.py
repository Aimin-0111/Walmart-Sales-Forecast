import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.express as px

# numeric columns only — Date and IsHoliday aren't histogram material
cols = ['Temperature', 'Fuel_Price',
        'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5',
        'Unemployment']   

fig, axes = plt.subplots(3, 3, figsize=(15, 10))
axes = axes.flatten()

for i, col in enumerate(cols):
    axes[i].scatter(df[col], df['CPI'], s=5, alpha=0.3)
    axes[i].set_xlabel(col)      # variable on x
    axes[i].set_ylabel('CPI')    # CPI on y
    axes[i].set_title(f'CPI vs {col}')

for j in range(len(cols), len(axes)):
    axes[j].axis('off')          # hide the leftover 9th panel

plt.tight_layout()
plt.show()
