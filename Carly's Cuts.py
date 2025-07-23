hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# What was the average price of a hair cut last week?
print(f'Prices Last Week: {prices}')
total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)
print(f'Total Of All Haircut Prices: ${total_price:.2f}')
print(f'Number of Haircut Options: {len(prices)}')
print(f'Average Haircut Price: ${average_price:.2f}')
print('\n')

# The average price was higher than expected, time to cut prices
new_prices = [price - 5 for price in prices]
print(f'Prices Next Week: {new_prices}')
total_new_prices = 0
for price in new_prices:
  total_new_prices += price

average_new_prices = total_new_prices / len(new_prices)
print(f'Total Of All New Haircut Prices: ${total_new_prices:.2f}')
print(f'Number of Haircut Options: {len(new_prices)}')
print(f'Average Haircut Price: ${average_new_prices:.2f}')
print('\n')

# Now let's see how much we made last week
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f'Total Revenue: ${total_revenue:.2f}')

# How much was that per day?
average_daily_revenue = total_revenue / 7
print(f'Average Daily Revenue: ${average_daily_revenue:.2f}')
print('\n')
# We can do better! Let's advertise all the new haircuts offered next week that will be under $30
#new_list = [<what I want> for <each index> in <list> if <constraint>]
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f'Cuts under $30: {cuts_under_30}')