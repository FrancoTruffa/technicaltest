import pandas as pd
from datetime import datetime
import numpy as np

df = pd.read_csv('C:/Users/Naranja/Documents/Downloads/Desafio/dataset.csv')
df['summary_date'] = pd.to_datetime(df['summary_date']).dt.strftime('%Y-%m-%d')
print("summary_date with ISO Date Format: \n", df['summary_date'])
df.drop(['event_name', 'events_d0', 'events_d7', 'unique_events_d0', 'unique_events_d7'], axis=1, inplace=True)
print("Valores nulos: \n", df.isnull().sum())
df = df.fillna(0)

number_impressions = df.groupby('campaign_id')["impressions"].sum()
print("Number of impressions: \n", number_impressions)
number_clicks = df.groupby('campaign_id')["clicks"].sum()
print("Number of clicks: \n", number_clicks)
number_installs = df.groupby('campaign_id')["installs"].sum()
print("Number of installs: \n", number_installs)
amount_spend = df.groupby('campaign_id')["spend"].sum()
print("Amount of spend: \n", amount_spend)
CTR = (number_clicks / number_impressions).replace(np.inf, np.nan).dropna()
print("CTR: \n", CTR)
CPI = (amount_spend / number_installs)
print("CPI: ", CPI)
