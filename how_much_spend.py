# Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.
# If item doesn't exist in the given cost values, the item is ignored.
# Output should be rounded to two decimal places.

# costs = {"socks": 5, "shoes": 60, "sweater": 30}
# get_total(costs, ['socks', 'shoes'], 0.09)

# -> 5+60 = 65
# -> 65 + 0.09 of 65 = 70.85
# -> Output: 70.85


def get_total(costs, items, tax):
    gross_cost = 0
    for item in items:
        if item in costs.keys():
            gross_cost += costs[
                item
            ]  # items in a dictionary are accessed using square brackets
    return round(gross_cost + tax * gross_cost, 2)


print(get_total({"socks": 5, "shoes": 60, "sweater": 30}, ["socks", "shoes"], 0.09))
