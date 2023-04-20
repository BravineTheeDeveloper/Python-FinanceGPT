# Import necessary libraries
import requests
import json

# Fetch cryptocurrency data using an API
# Replace 'API_KEY' with your actual API key
api_key = 'API_KEY'  # Replace with your actual API key
symbol = 'BTC'  # Example cryptocurrency symbol
url = f'https://api.twelvedata.com/quote?symbol={symbol}&apikey={api_key}'  # API endpoint for fetching cryptocurrency data
response = requests.get(url)  # Send HTTP GET request to the API endpoint
crypto_data = json.loads(response.text)  # Parse the API response as JSON and store in a dictionary

# Extract relevant cryptocurrency information
symbol = crypto_data['symbol']  # Extract symbol from the API response
price = crypto_data['price']  # Extract price from the API response
volume = crypto_data['volume']  # Extract volume from the API response
# ... (extract other relevant information from the API response)

# Display cryptocurrency information
print(f'Symbol: {symbol}')
print(f'Price: {price}')
print(f'Volume: {volume}')
# ... (print other relevant information)
