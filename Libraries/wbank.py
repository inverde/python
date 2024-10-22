"""
We could also search for economic, social and development data
in the World Bank """
import sys, os
import requests
# World Bank Web Site
url = "https://api.worldbank.org/v2"


indicator_dir = {
    'GDP':'NY.GDP.MKTP.CD,
    'GNI':'NY.GNI.TOTL.CD,
    'CPI':'FP.CPI.TOTL.ZG'
}

params = {'country':country, 'indicator':indicator, 'format':'json'}




