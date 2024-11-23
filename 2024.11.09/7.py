from ref7 import list_of_dicts

total_dict={}

for a in list_of_dicts:
    for name, key in a.items():
        if name in total_dict:
            total_dict[name].add(key)
        else:
            total_dict[name]={key}

for name, key in total_dict.items():
    print(f'{name}:{key}')
    
#Владивосток:{5}
#Воронеж:{1, 4}
#Екатеринбург:{1, 3, 5}
#Иркутск:{9, 2, 5}
#Москва:{3, 4, 6}
#Новокузнецк:{2, 4}
#Оренбург:{1}
#Саратов:{2}
#Уфа:{9}
#Ярославль:{8, 7}
#Волгоград:{5}
#Нижний Новгород:{8, 2, 5}
#Ростов-на-Дону:{6}
#Тольятти:{1}
#Тюмень:{3}
#Казань:{4}
#Новосибирск:{7}
#Пермь:{3}
#Челябинск:{3}
#Санкт-Петербург:{7}