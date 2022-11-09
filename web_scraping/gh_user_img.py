import requests
from bs4 import BeautifulSoup as bs

gh_user = input("Input github user: ")
url = f'https://github.com/{gh_user}'
req  = requests.get(url)
soup = bs(req.content, 'html.parser') # the content part returns the source code as well
profile_img = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_img)