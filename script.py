import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

source_url = "https://soaring.de/osclass/index.php?page=search&sPattern=altimeter+57"
page = urlopen(source_url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

card_list = soup.select('.listing-card')

mapped_cards = []

for card in card_list:
    link_tag = card.select_one('.listing-thumb')
    url = link_tag.get('href')
    title = link_tag.get('title')
    listing_item = {'title':title, 'url': url}
    
    mapped_cards.append(listing_item)

# Export the array to a JSON file
with open("output.json", "w") as json_file:
    json.dump(mapped_cards, json_file, indent=4)  # Use `indent` for pretty printing

print("Array exported to output.json")