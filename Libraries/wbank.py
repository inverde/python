"""
We could also search for economic, social and development data
in the World Bank """
import sys, os
import requests
# World Bank Web Site
url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"


indicator_dir = {
    'GDP':'NY.GDP.MKTP.CD,
    'GNI':'NY.GNI.TOTL.CD,
    'CPI':'FP.CPI.TOTL.ZG'
}

country = 'dom'
indicator = indicator_dir['GDP']

params = {'country':country, 'indicator':indicator, 'format':'json'}

response = requests.get(url, params=params)

data = response.json()

if response.status_code == 200:
    print(data)


