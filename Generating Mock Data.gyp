import pandas as pd
import numpy as np
import random

salesID = []

while len(salesID) < 500:
    generate_ID = (random.randrange(5000,6001))
    if generate_ID not in salesID:
        salesID.append(generate_ID)


#print(salesID)

import names

#print(names.get_full_name())

def create_data_int(col_name):
    generateInt = (random.randrange())
    if generateInt not in col_name:
        col_name.append(generateInt)
    


import random
columns = ['Serial_Number' , 'Product_Type' , 'Product_Date' , 'Units_Sold' , 'Product_Price' , 'Product_Inventory_Amt']

product_types = ['lettuce', 'apples', 'oranges', 'peaches', 'pears',
 'prunes', 'plums', 'strawberries', 'raisins', 'kiwi', 'pineapple', 
 'bananas', 'cauliflower', 'broccoli', 'carrots', 'garlic', 'celery',
 'green peppers', 'corn', 'tomatoes', 'mushrooms', 'rice', 'canned vegetables',
 'cheese', 'hamburger', 'butter', 'chicken', 'fresh fish', 'pork chops', 
 'pork and beans', 'meat balls', 'lunch meat', 'wieners', 'wiener buns', 
 'eggs', 'bread', 'butter', 'jelly', 'cheese', 'potatoes', 'pasta', 'ketchup',
 'yogurt', 'cottage cheese', 'cereal', 'milk', 'orange juice', 'apple juice', 
 'prune juice', 'ice cream', 'soda', 'soup', 'macaroni and cheese', 'oatmeal', 
 'chocolate milk', 'bread', 'mayonnaise', 'mustard', 'rice', 'laundry soap', 
 'dish soup', 'dishwasher soap', 'tissue', 'toilet paper', 'paper towels', 
 'beer', 'cigarettes', 'cake mixes', 'crackers', 'chocolate chips', 'hot chocolate mix', 
 'coffee', 'tea', 'cooking oil', 'vinegar', 'flour', 'sugar', 'salt', 'pepper', 'onions', 
 'cinnamon', 'ginger', 'onion salt', 'garlic powder', 'bakery foods', 'baking soda', 'flour', 
 'vanilla', 'cake mixes', 'noodles', 'spaghetti', 'potato chips', 'diapers', 'sponges', 
 'baby formula', 'strained baby food', 'baby lotion', 'hand lotion', 'batteries', 'newspaper', 'magazines'
]


#Creating product ID
product_id = []

while len(product_id) < len(product_types):
    generate_ID = (int(random.randrange(5000,6001)))
    if generate_ID not in product_id:
        product_id.append(generate_ID)

#Creating Product Price
product_price = []
for i in range(0,len(product_types)):
    product_price.append(int(random.randrange(1,11)))

print(type(product_price[0]))
from datetime import date
today = date.today()

#Creating Date
# dd/mm/YY

d1 = today.strftime("%d/%m/%Y")
product_date = [d1] * len(product_types)



units_sold = [0] * len(product_types)
product_inventory_amount = [500] * len(product_types)

df = pd.DataFrame(columns=columns)
print(list(df))
data = [product_id,product_types,product_date,units_sold, product_price , product_inventory_amount]
df['Serial_Number'] =  product_id
df['Product_Type'] = product_types
df['Product_Date'] = product_date
df['Units_Sold'] = units_sold
df['Product_Price'] = product_price
df['Product_Inventory_Amt'] = product_inventory_amount
#print(product_price)
print(df)

df.to_csv("Products.csv")



