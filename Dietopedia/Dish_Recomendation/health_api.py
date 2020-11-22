import json
import urllib.parse
import urllib.request
import random
import requests
from Dish_Recomendation.recipe import *

APP_ID = "3b47c8ec"
API_KEY = "84f014c706c1ea02fd6226da1078c53f"
URL_BASE = 'https://api.edamam.com/diet?'
#   https://api.edamam.com/diet?%3Fq=Apple&app_id=3b47c8ec&app_key=84f014c706c1ea02fd6226da1078c53f&to=150
# https://api.edamam.com/diet?q=chicken&app_id=3b47c8ec&app_key=84f014c706c1ea02fd6226da1078c53f&from=0&to=3&health=alcohol-free
Name_Food= "meals"
def create_url():
    return URL_BASE + "&q=" + Name_Food + "&app_id=" + APP_ID + "&app_key=" + API_KEY + "&to=100"
    

def add_health_restrictions(url:str, flags:list):
    ''' rest [dairy-free, kosher, kidney-friendly, etc] ''' 
    for rest in flags:
        url+="&Health=" + rest
    return url




def get_result(url: str)->dict:
    '''this will recieve the json text'''
    response = None
    try:
        response = requests.get(url, auth=('user', 'pass'))
        #json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(response.text)
    finally:
        if response != None:
            response.close()



def add_recipe(json:dict, cal_goal:int):
    choice = random.randrange(0, len(json['hits']))
    r = Recipe(json['hits'][choice])
    
    while (r['calories'] > cal_goal/3) or (r['calories'] < 30):
        choice = random.randrange(0, len(json['hits']))
        r = Recipe(json['hits'][choice])  
    
    return r