import json
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

source_url = "https://soaring.de/osclass/index.php?page=search&sOrder=dt_pub_date&iOrderType=desc&sPattern=altimeter+57&sPriceMax=1000"

page = urlopen(source_url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

card_list = soup.select('.listing-card')

with open('listing-archive.json', 'r') as json_file:
    listing_archive = json.load(json_file)

current_items = []

for card in card_list:
    link_tag = card.select_one('.listing-thumb')
    url = link_tag.get('href')
    title = link_tag.get('title')
    listing_item = {'title':title, 'url': url}
    
    current_items.append(listing_item)

today = datetime.today().strftime('%Y-%m-%d')

listing_archive[today] = current_items

# Export the array to a JSON file
with open("listing-archive.json", "w") as json_file:
    json.dump(listing_archive, json_file, indent=4)

archive_properties_list = list(listing_archive.keys())
todays_listings_index = archive_properties_list.index(today)

previous_listings_index = todays_listings_index - 1
prevous_listings_key = archive_properties_list[previous_listings_index]

previous_listings = listing_archive[prevous_listings_key]

# Array of urls 
previous_urls = {listing["url"] for listing in previous_listings}

new_items = [listing for listing in current_items if listing["url"] not in previous_urls]

print(json.dumps(new_items, indent = 4))

# Import list and compare it with new one