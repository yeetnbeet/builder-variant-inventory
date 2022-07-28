import os ;
import csv ;
import json
from typing import Counter ; 
import requests;
from dotenv import load_dotenv ;

#currently it takes all the products in a collection and gets the ID for them
#then it will get the 

load_dotenv()
#GLOBALS make this and interface class at some point
key = os.getenv("SECRET_TOKEN")
URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/collections/291616489658/products.json?"
H = {"X-Shopify-Access-Token":key}

def getProductsFromCollection(collectionID):
    URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/collections/"+str(collectionID)+"/products.json?" #TODO eventually add collection ID
    res = requests.get(URLForCollection,headers=H)
    resdata = res.json()
    idList = []
    for i in resdata["products"]:
        print("\n",i,"\n")
        idList.append(i["id"])

    return idList

def getSKU_Inventory(idList):
    URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/products/7152450109626/variants.json"
    res = requests.get(URLForCollection,headers=H)
    resdata = res.json()
    print()
    print(resdata["variants"])
    return 0

print(getProductsFromCollection(291616489658))
print(getSKU_Inventory(1))




