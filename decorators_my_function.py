import os
from datetime import datetime
from Heroes_int import *

def logger(old_function):
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        old_function_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('my_function.log', 'w', encoding='utf-16') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {old_function_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result
    return new_function 


@logger
def rating_intelligence(name_hero):
    hero_dict = hero_intelligence_dict(name_hero)
    sorted_values = sorted(hero_dict.values(), reverse=True)
    
    for hero_intell in hero_dict.items():
        if hero_intell[1] == sorted_values[0]:
            first_hero =  hero_intell[0]
    return first_hero


if __name__ == '__main__':
    name_hero = ['Hulk', 'Captain America', 'Thanos']  
    rating_intelligence(name_hero)
