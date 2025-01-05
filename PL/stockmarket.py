import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime

# Configurations
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")


# List of stocks
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Date range
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

# Download stock data into a dictionary
stock_data = {}
for stock in tech_list:
    stock_data[stock] = yf.download(stock, start, end)

# Add company name and combine all data into a single DataFrame
company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
company_list = []

for stock, name in zip(tech_list, company_name):
    temp_df = stock_data[stock]
    temp_df['company_name'] = name
    company_list.append(temp_df)

df = pd.concat(company_list, axis=0)

# Display the last 10 rows
print(df.tail(10))
