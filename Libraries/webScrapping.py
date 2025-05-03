# Web Scrapping module created  on May 2, 20025
import requests
from bs4 import BeautifulSoup

# Write the url content to destination source
url = 'https://cs50.harvard.edu/python/2022/notes/7'

response = requests.get(url)
html_content = response.text

# Get the soup of object out the html document
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()


def stripspace_from_text_to_list(text:str)->list:
    # List for comprehension to strip blank lines for text
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return lines

def main():
    global text
    lines = stripspace_from_text_to_list(text)
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
