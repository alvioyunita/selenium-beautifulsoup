import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.python.org/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div containing the list of upcoming events (under "What's New")
    news_section = soup.find('div', class_='medium-widget event-widget last')

    # Find all list items in that section
    items = news_section.find_all('li')

    # Print the news titles and links
    for item in items:
        title = item.find('a').get_text(strip=True)
        link = item.find('a')['href']
        print(f"- {title}: https://www.python.org{link}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
