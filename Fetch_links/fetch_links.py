import requests
from bs4 import BeautifulSoup


url = input() # google.com 

# Sending GET method request to the url
response = requests.get(url)

# Optional
response.encoding = 'utf-8'

# Parsing HTML response 
soup = BeautifulSoup(response.content, "html.parser")
links = []

# Extracting links in hre from anchor tags
for link in soup.find_all('a'):
    links.append(link.get('href'))

# Writing links into text file
with open('links.txt', 'w') as f:
    f.writelines('\n'.join(links))

