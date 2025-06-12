import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'

response = requests.get(url)

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

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the footer
    footer = soup.find('li', class_='tier-1 element-2')
    footer = footer.find_all('li', class_="tier-2")

    datanya = []
    for item in footer:
        link = item.find('a')
        if link:
            text = link.get_text(strip=True)
            href = link['href']
            datanya.append(text)

    print(datanya)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")