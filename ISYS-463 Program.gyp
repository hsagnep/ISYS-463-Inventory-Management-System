import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


#Creating database
conn = sqlite3.connect('ISYS463.db')
c = conn.cursor()

#Creating tables
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Customer(first_name VARCHAR, last_name VARCHAR,phone_number INT, email_address VARCHAR, rewards_members BOOL)")
    c.execute("CREATE TABLE IF NOT EXISTS Retailer(RetailerID INT , Retailer_Name VARCHAR, Retailer_Address VARCHAR, Retailer_Capacity INT, Retailer_Region VARCHAR)")
    c.execute("CREATE TABLE IF NOT EXISTS Product(Serial_Number INT, Product_Type VARCHAR , Product_Date VARCHAR, Units_Sold INT, Product_Price FLOAT, Product_Inventory_Amt INT)")
create_table()

#Creating a class for each entity
class Customer():
    def __init__(self,first_name ,last_name , phone_number , email_address , rewards_member):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.rewards_member = rewards_member

    def insert_into_table(self):
        customer_data = (self.first_name , self.last_name , self.phone_number , self.email_address , self.rewards_member)
        c.execute("INSERT INTO Customer VALUES(? , ? , ? , ? , ?)",customer_data)
        conn.commit()
    
"""
class Transaction(Customer, Product, Retailer):
    def __init__ (self, transation_id):
        self.transation_id = transation_id
        self.first_name = first_name
        self.last_name = last_name
        self.RetailerID = RetailerID
        self.Retailer_Address = Retailer_Address

    def create_reciept(self):
        pass
"""

class Retailer():
    def __init__(self , RetailerID , Retailer_Name , Retailer_Address , Retailer_Capacity , Retailer_Region):
        self.RetailerID = RetailerID
        self.Retailer_Name = Retailer_Name
        self.Retailer_Address = Retailer_Address
        self.Retailer_Capacity = Retailer_Capacity
        self.Retailer_Region = Retailer_Region
    
    def insert_into_table(self):
        retailer_data = (self.RetailerID , self.Retailer_Name , self.Retailer_Address , self.Retailer_Capacity, self.Retailer_Region)
        c.execute("INSERT INTO Retailer VALUES(? , ? , ? , ? , ?)",retailer_data)
        conn.commit()


class Product():
    def __init__(self , Serial_Number , Product_Type , Product_Date , Units_Sold , Product_Price , Product_Inventory_Amt):
        self.Serial_Number = Serial_Number
        self.Product_Type = Product_Type
        self.Product_Date = Product_Date
        self.Units_Sold = Units_Sold
        self.Product_Price = Product_Price
        self.Product_Inventory_Amt = Product_Inventory_Amt

    def insert_into_table(self):
        product_data = (self.Serial_Number , self.Product_Type , self.Product_Date , self.Units_Sold , self.Product_Price , self.Product_Inventory_Amt)
        c.execute("INSERT INTO Product VALUES(? , ? , ? , ? , ? , ?)" , product_data)
        conn.commit()

Customer_1 = Customer('Hervin' , 'Sagnep' , 5102287268 , 'hervinsagnep@gmail.com' , 1)
Retailer_1 = Retailer(5001 , "Lucky" , "675 Blossom Way" , 600 , "CA")
Product_1 = Product(200012 , "Fruit" , "04-20-2020" , 300 , 2.87 , 600)

Customer_1.insert_into_table()
Retailer_1.insert_into_table()
Product_1.insert_into_table()

#Front-End
#Needed functionality
#Calculating the mean
#Graphing sales data


#Inserting Mock Data
df = pd.read_csv("/Users/hervinsagnep/Documents/ISYS\ Project/Products.csv")
def insert_products(df):
    for i in range(0,len(df)):
        product = Product(df.loc[i][0], df.loc[i][1] , df.loc[i][2] , df.loc[i][3] , df.loc[i][4] , df.loc[i][5])
        product.insert_into_table()
insert_products(df)






