"""Write one line of Python that takes this list and makes a new list that has only the even elements
of this list in it."""

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even_numbers = []
# for number in numbers:
#     if number %2 == 0:
#         even_numbers.append(number)
# print(even_numbers)

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Practice with list comprehensions
# tags = []
# tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
# for div in tags_divs:
#     tags.append(div.text_content())
# tags = [tag.split(', ') for tag in tags]
#
# platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
# total_platforms = []