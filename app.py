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

#input the collection ID and it gives a list of product IDs
def getProductsFromCollection(collectionID):
    URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/collections/"+str(collectionID)+"/products.json?" #TODO eventually add collection ID
    res = requests.get(URLForCollection,headers=H)
    resdata = res.json()
    idList = []
    for i in resdata["products"]:
        idList.append(i["id"])

    return idList

#input the list of Product IDs and it outputs a list of SKU and Inventory id for each variant
def getSKU_Inventory(idList):
    inventorylist = []
    counter = 0
    for id in idList:
        URLForCollection = "https://sams-test-store-app.myshopify.com/admin/api/2022-10/products/"+str(id)+"/variants.json"
        res = requests.get(URLForCollection,headers=H)
        resdata = res.json()
        time.sleep(.3)
        counter += 1
        for item in resdata["variants"]:
            print("SKU: ",item['sku'],"\n")
            print(item['inventory_item_id']," quant:",item['inventory_quantity'],"\n-------------------")
            inventorylist.append([item["sku"],item["inventory_item_id"]])
    
    return inventorylist
#input the list of SKU and Inventory and It will output a matrix of [Sku,InventoryId,inventoryID1,inventoryID2,inventoryID3...] 
def getInventoryLevel(inventoryList):
    locations = [] #[[locationname1,locationID1],[locationname2,locationID2]]
    res = requests.get("https://sams-test-store-app.myshopify.com/admin/api/2022-10/locations.json",headers=H)
    resdata = res.json()

    for line in resdata["locations"]:
        locations.append(line["id"])

    for line in inventoryList:
        #TODO iterate thru the SKU and inventory ID and fill the matrix
        print(line)

    return locations

idlist=getProductsFromCollection(291616489658)
framesList = getSKU_Inventory(idlist)
framesList.pop(0)
print(getInventoryLevel(framesList))
for i in framesList:
    print(i)




