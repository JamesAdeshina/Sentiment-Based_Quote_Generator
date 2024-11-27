import pandas as pd
quotes = pd.read_csv('data/quote_stash.csv')

quotes = quotes[['quote','author']]

quotes.head()

print(quotes.head())




