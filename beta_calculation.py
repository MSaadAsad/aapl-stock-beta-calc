import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# File paths for Apple's stock data and S&P 500 data.
apple_file_path = "/Users/muhammadsaadasad/Downloads/AI Lab/AAPL.csv"
sp500_file_path = "/Users/muhammadsaadasad/Downloads/AI Lab/S&P 500 Historical Data 6.43.25 PM.csv"

# Load data into dataframes.
apple_data = pd.read_csv(apple_file_path)
sp500_data = pd.read_csv(sp500_file_path)

# Drop the last 138 records from the apple dataset.
apple_data = apple_data.drop([index for index in range(5000, 5138)])

# Display the first five records from the datasets
print(apple_data.head())
print(sp500_data.head())

# Create a list of 'Adjusted Close' prices of Apple and 'Price' of S&P 500.
apple_prices = list(apple_data["Adj Close"])
sp500_prices = list(sp500_data["Price"])
sp500_prices.reverse()

# Function to remove non-digits from a string.
def remove_non_digits(seq):
    seq_type = type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

# Clean 'sp500_prices' by removing non-digits and converting strings to integers.
cleaned_sp500_prices = [int(remove_non_digits(price))/100 for price in sp500_prices]

# Calculate returns for both Apple and S&P 500.
apple_returns = []
sp500_returns = []

for i in range(1, 5000):
    apple_returns.append(100 * (apple_prices[i] - apple_prices[i-1]) / apple_prices[i-1])
    sp500_returns.append(100 * (cleaned_sp500_prices[i] - cleaned_sp500_prices[i-1]) / cleaned_sp500_prices[i-1])

# Calculate beta for each year and store it in a list.
beta_list = []

for i in range(5, 20):
    apple_returns_subset = np.array(apple_returns[((i-5)*260):(i*260)])
    sp500_returns_subset = np.array(sp500_returns[((i-5)*260):(i*260)])
    
    # Calculate covariance and variance.
    covariance = np.cov(apple_returns_subset, sp500_returns_subset)[0][1]
    sp500_variance = np.var(sp500_returns_subset)
    
    # Calculate beta.
    beta = covariance / sp500_variance
    beta_list.append(beta)

# Create a dataframe to display the years and the calculated beta.
years = [year for year in range(2008, 2023)]
beta_df = pd.DataFrame({"years": years, "beta": beta_list})

# Set 'years' as the index of the dataframe.
beta_df.set_index("years")
