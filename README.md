Project Overview: Calculating Historical Betas for Apple Inc.
This project was undertaken as part of a larger initiative to understand the sensitivity of stock market prices with respect to various financial metrics. The primary focus of this particular part was to calculate the historical beta values for Apple Inc.

Project Background
In finance, the Beta (β) of an investment is a measure of the investment's risk in relation to the market. A beta less than 1 indicates the investment is less volatile than the market, while a beta greater than 1 indicates the investment is more volatile.

Calculating beta for a specific year or period can provide insights into the volatility of the stock during that timeframe, relative to the overall market volatility. This is especially useful for portfolio risk management and financial analysis.

Unfortunately, some of these financial metrics are behind paywalls and needed to be computed manually. The primary aim of this codebase was to calculate these beta values for Apple Inc., over a range of years.

Data Sources
We sourced historical stock market data for both Apple Inc. and the S&P 500 index. Here are the sources for our datasets:

S&P 500 Historical Data: Investing.com
Apple Inc. Historical Data: Yahoo Finance
Implementation
The code reads historical stock price data for Apple Inc. and the S&P 500 index, then calculates the returns for both. After that, it calculates the Beta value for each year by computing the ratio of covariance of the returns to the variance of the S&P 500 returns. This is done over a rolling window of years to create a timeseries of beta values.

Results
Using this method, we were able to estimate historical beta values for Apple Inc. that were relatively close to actual beta values for the given years. For instance, our estimate for the beta in the year 2022 was 1.22, which was only 5.5% off from the actual beta of 1.29 for that year.

This validates the effectiveness of our implementation and sets a positive precedent for its use in calculating historical beta values for other stocks as well.
