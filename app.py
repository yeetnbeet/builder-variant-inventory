import os ;
import csv ;
import json
from typing import Counter ; 
import requests;
from dotenv import load_dotenv ;
import time ;

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
        idList.append(i["id"])

    return idList

#TODO the first item returned in inventory list has no sku?
def getSKU_Inventory(idList):
    inventorylist = []
    counter = 0
    for id in idList:
        URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/products/"+str(id)+"/variants.json"
        res = requests.get(URLForCollection,headers=H)
        resdata = res.json()
        time.sleep(1)
        counter += 1
        for item in resdata["variants"]:
            print("SKU: ",item['sku'],"\n")
            print(item['inventory_item_id']," quant:",item['inventory_quantity'],"\n-------------------")
            inventorylist.append([item["sku"],item["inventory_item_id"]])
    
    
    
    return inventorylist

idlist=getProductsFromCollection(291616489658)
framesList = getSKU_Inventory(idlist)
for i in framesList:
    print(i)




