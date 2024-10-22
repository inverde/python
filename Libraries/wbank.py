"""
We could also search for economic, social and development data
in the World Bank """
import sys, os
import requests

indicator_dir = {
    'GDP':'NY.GDP.MKTP.CD',
    'GNI':'NY.GNI.TOTL.CD',
    'CPI':'FP.CPI.TOTL.ZG'
}
country = 'dom'
indicator = indicator_dir['GDP']

# World Bank Web Site
url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"



params = {'country':country, 'indicator':indicator, 'format':'json'}

response = requests.get(url, params=params)

data = response.json()

if response.status_code == 200:
    results = data[1]
    stats = []
    for result in results:
        indicator = result['indicator']['value']
        country_code = result['countryiso3code']
        publish_year = result['date']
        val = result['value']
        stat = {
            'stat':indicator,
            'country':country_code,
            'date':publish_year,
            'value':float(f"{val//1000000:,.0f}".replace(',', '')),
            'units':'Mills'
        }
        stats.append(stat)
        print(stat)


