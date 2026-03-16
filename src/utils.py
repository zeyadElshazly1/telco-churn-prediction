import pandas as pd
import matplotlib.pyplot as plt
import os

def load_raw_data(path='data/raw/telco_churn.csv'):
    df = pd.read_csv(path)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    return df

def save_figure(filename, folder='outputs/figures'):
    os.makedirs(folder, exist_ok=True)
    plt.savefig(f'{folder}/{filename}', dpi=150, bbox_inches='tight')
    print(f"Saved: {folder}/{filename}")