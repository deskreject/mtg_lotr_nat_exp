### Author: Alexander Staub
### Date: 2021-08-25
### Description: use scryfall api to get price data for mtg cards

#importing packages
import os
import pandas as pd
import requests


#set working directory


##bard code

# define the function to get the price data
def get_mtg_price_data(card_name):
    url = "https://api.scryfall.com/cards/named?name=" + card_name
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]
        recent_prices = prices[-7:]
        return recent_prices
    else:
        return None

def main():
    card_name = "Aragorn, the Uniter"
    recent_prices = get_mtg_price_data(card_name)
    if recent_prices is not None:
        for price in recent_prices:
            print(price["date"], price["usd"])

if __name__ == "__main__":
    main()
