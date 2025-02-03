# Sample data: Dictionary with items as keys and their prices as values
shop_items = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# Sort the dictionary by values (prices) in descending order. The sorted function returns a list of tuples.
# Each tuple contains a key-value pair where the key is the item name and the value is the price.
sorted_items = sorted(shop_items.items(), key=lambda x: x[1], reverse=True)

# Print the top 3 items and their prices. The slice [0:3] gives us the top 3 items.
for item in sorted_items[:3]:
    print(f"{item[0]} {item[1]}")
