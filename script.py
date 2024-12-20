from bs4 import BeautifulSoup
from urllib.request import urlopen

source_url = "https://soaring.de/osclass/index.php?page=search&sPattern=altimeter+57"
page = urlopen(source_url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

card_list = soup.select('.listing-card')

mapped_cards = []

class ListingItem:
    # Constructor to initialize the object
    def __init__(self, title, link):
        self.title = title
        self.link = link

for card in card_list:
    link_tag = card.select_one('.listing-thumb')
    url = link_tag.get('href')
    title = link_tag.get('title')
    mapped_cards.append(card)

    result = ListingItem(title, url)
    print(result.title)