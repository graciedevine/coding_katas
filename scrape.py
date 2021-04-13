import requests
import lxml.html

# Open the webpage.
html = requests.get('https://store.steampowered.com/explore/new/')
# Makes HTML-type element into object.
doc = lxml.html.fromstring(html.content)
# Returns list of all divs in HTML page with tab_newreleases_content id. First element is our required div.
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

"""Extracts titles and prices."""
# Returns titles of all games in the "Popular New Releases" tab.
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
# Returns prices of all games in the "Popular New Releases" tab.
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

"""Extracts tags associated with titles"""
tags = []
# Loops over extracted tags, extracts text, returns text without HTML markup.
for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]'):
    tags.append(tag.text_content())

"""Extracts platforms associated with each title."""
tags = [tag.split(', ') for tag in tags]
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    # Returns spans regardless of any additional classes with a particular tag.
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    # Uses .get() to extract the class attribute of a span.
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    # Removes hmd_separator
    total_platforms.append(platforms)

output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {'title': info[0], 'price': info[1], 'tags': info[2], 'platforms': info[3]}
    output.append(resp)

print(output)
