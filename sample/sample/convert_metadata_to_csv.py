import csv

# Data to be written into the CSV
data = [
    ["Location", "Department", "Category", "SubCategory"],
    ["Perimeter", "Bakery", "Bakery Bread", "Bagels"],
    ["Perimeter", "Bakery", "Bakery Bread", "Baking or Breading Products"],
    ["Perimeter", "Bakery", "Bakery Bread", "English Muffins or Biscuits"],
    ["Perimeter", "Bakery", "Bakery Bread", "Flatbreads"],
    ["Perimeter", "Bakery", "In Store Bakery", "Breakfast Cake or Sweet Roll"],
    ["Perimeter", "Bakery", "In Store Bakery", "Cakes"],
    ["Perimeter", "Bakery", "In Store Bakery", "Pies"],
    ["Perimeter", "Bakery", "In Store Bakery", "Seasonal"],
    ["Center", "Dairy", "Cheese", "Cheese Sauce"],
    ["Center", "Dairy", "Cheese", "Specialty Cheese"],
    ["Center", "Dairy", "Cream or Creamer", "Dairy Alternative Creamer"],
    ["Center", "Dairy", "Cream or Creamer", "Whipping Creams"],
    ["Center", "Dairy", "Cultured", "Cottage Cheese"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Breads"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated English Muffins and Biscuits"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Hand Held Sweets"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Pie Crust"],
    ["Center", "Dairy", "Refrigerated Baking", "Refrigerated Sweet Breakfast Baked Goods"],
    ["Perimeter", "Deli and Foodservice", "Self Service Deli Cold", "Beverages"],
    ["Perimeter", "Deli and Foodservice", "Service Deli", "Cheese All Other"],
    ["Perimeter", "Deli and Foodservice", "Service Deli", "Cheese American"],
    ["Perimeter", "Floral", "Bouquets and Cut Flowers", "Bouquets and Cut Flowers"],
    ["Perimeter", "Floral", "Gifts", "Gifts"],
    ["Perimeter", "Floral", "Plants", "Plants"],
    ["Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"],
    ["Center", "Frozen", "Frozen Bake", "Breakfast Cake or Sweet Roll Frozen"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Entrees"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Breakfast Sandwich"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Egg Substitutes"],
    ["Center", "Frozen", "Frozen Breakfast", "Frozen Syrup Carriers"],
    ["Center", "Frozen", "Frozen Desserts or Fruit and Toppings", "Pies Frozen"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Apple Juice"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Fruit Drink Mixers"],
    ["Center", "Frozen", "Frozen Juice", "Frozen Fruit Juice All Other"],
    ["Center", "GM", "Audio Video", "Audio"],
    ["Center", "GM", "Audio Video", "Video DVD"],
    ["Center", "GM", "Audio Video", "Video VHS"],
    ["Center", "GM", "Housewares", "Bedding"],
    ["Center", "GM", "Housewares", "Candles"],
    ["Center", "GM", "Housewares", "Collectibles and Gifts"],
    ["Center", "GM", "Housewares", "Flashlights"],
    ["Center", "GM", "Housewares", "Frames"],
    ["Center", "GM", "Insect and Rodent", "Indoor Repellants or Traps"],
    ["Center", "GM", "Insect and Rodent", "Outdoor Repellants or Traps"],
    ["Center", "GM", "Kitchen Accessories", "Kitchen Accessories"],
    ["Center", "GM", "Laundry", "Bleach Liquid"],
    ["Center", "GM", "Laundry", "Bleach Powder"],
    ["Center", "GM", "Laundry", "Fabric Softener Liquid"],
    ["Center", "GM", "Laundry", "Fabric Softener Sheets"],
    ["Center", "Grocery", "Baking Ingredients", "Dry or Canned Milk"],
    ["Center", "Grocery", "Baking Ingredients", "Food Coloring"],
    ["Center", "Grocery", "Spices", "Salt Cooking or Edible or Seasoned"],
    ["Center", "Grocery", "Spices", "Salt Substitute"],
    ["Center", "Grocery", "Spices", "Seasoning Dry"],
    ["Center", "Grocery", "Stuffing Products", "Stuffing Products"],
    ["Perimeter", "Seafood", "Frozen Shellfish", "Frozen Shellfish"],
    ["Perimeter", "Seafood", "Other Seafood", "All Other Seafood"],
    ["Perimeter", "Seafood", "Other Seafood", "Prepared Seafood Entrees"],
    ["Perimeter", "Seafood", "Other Seafood", "Seafood Salads"],
    ["Perimeter", "Seafood", "Other Seafood", "Smoked Fish"],
    ["Perimeter", "Seafood", "Other Seafood", "Seafood Breading Sauces Dips"]
]

# Specify the file name
filename = 'locations.csv'

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to {filename}")