from itertools import count
import os ;
import json
from typing import Counter ; 
import requests;
from dotenv import load_dotenv ;

#currently it takes all the products in a collection and gets the ID for them
#then it will get the 

load_dotenv()
#GLOBALS
key = os.getenv("SECRET_TOKEN")
URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/collections/291616489658/products.json?"
H = {"X-Shopify-Access-Token":key}

def getProductsFromCollection(collectionID):
    URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/collections/291616489658/products.json?" #TODO eventually add collection ID
    res = requests.get(URLForCollection,headers=H)
    resdata = res.json()
    idList = []
    for i in resdata["products"]:
        idList.append(i["id"])

    return idList 

print(getProductsFromCollection(1))
