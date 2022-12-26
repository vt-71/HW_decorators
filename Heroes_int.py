from pickle import TRUE
from pprint import pprint
import requests


def hero_request(name):
# Получение данных по запросу
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    heroes = response.json()
    for hero in heroes:
        if hero['name'] == name:
            intelligence = hero['powerstats']['intelligence']
    return intelligence

def rating_intelligence():
    #Функция сортировки и определения рейтинга по интеллекту 
    name_hero = ['Hulk', 'Captain America', 'Thanos']         
    hero_dict = hero_intelligence_dict(name_hero)
    # print(f'Я в функции {hero_dict}')
    sorted_values = sorted(hero_dict.values(), reverse=True)
    sorted_dict = {}

    for hero_intell in hero_dict.items():
        if hero_intell[1] == sorted_values[0]:
            first_hero =  hero_intell[0]
    return first_hero

def hero_intelligence_dict(name_hero):   
    hero_intelligence_dict = {}
    for hero in name_hero:
        hero_intelligence_dict[hero] =  hero_request(hero) 
    return hero_intelligence_dict
            

if __name__ == '__main__':    
    # name_hero = ['Hulk', 'Captain America', 'Thanos']       
    # print(f'Наиболее высокий интеллект у {rating_intelligence()}')
   rating_intelligence()     





        




