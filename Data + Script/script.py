# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:43:43 2020

@author: Zayd Alameddine
"""

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv('NFLX.csv')
dowjones_stocks = pd.read_csv('DJI.csv')
netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')

# renamed this column to make it easier to use since the Adj Close is really just the actual price of the stock
netflix_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
dowjones_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
netflix_stocks_quarterly.rename(columns = {'Adj Close': 'Price'}, inplace = True)

# Visualizing the distribution of the Netflix quarterly stock
ax = sns.violinplot(x = 'Quarter', y = 'Price', data = netflix_stocks_quarterly)
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set(xlabel='Closing Stock Price', ylabel = 'Business Quarters in 2017')

plt.show()
plt.savefig('QuarterlyDistribution.png')
# deletes the previous plot
plt.clf()

# Charting the performance of the earnings per chare (EPS) by graphing the estimated Yahoo projected for the Quarter compared to the actual earnings for that quarter

# All the information that will be needed to plot the chart
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

# Ploting the actual vs estimated earnings
plt.scatter(x_positions, earnings_actual, c='red', alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, c='blue', alpha = 0.5)

# Labeling the plot
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')

plt.show()
plt.savefig('EarningsPerShare.png')
# deletes the previous plot
plt.clf()

# Plot of earnings and revenue reported by Netflix

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]



# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)

# Adding titles and labels to the plot 
plt.legend(labels)
plt.title('Earnings and Revenue Per Quarter')

plt.xticks(middle_x, quarter_labels)

plt.show()
plt.savefig('Earnings&RevenuePerQuarter')
# deletes the previous plot
plt.clf()

# Comparing the Netflix stock to the Dow Jones Industrial Average in 2017

# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])

ax1.set_title('Netflix')
ax1.set(xlabel='Date', ylabel = 'Stock Price')

# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])

ax2.set_title('Dow Jones')
ax2.set(xlabel='Date', ylabel = 'Stock Price')


plt.subplots_adjust(wspace=.5)

plt.show()
plt.savefig('NetflixDowJonesComparison.png')

print(netflix_stocks.head(5))
print(dowjones_stocks.head(5))
print(netflix_stocks_quarterly.head(5))





















