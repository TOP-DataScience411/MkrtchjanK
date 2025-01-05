from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from utils import load_file

def ask_for_file() -> object:
   
    #Запрашивает у пользователя путь к файлу и копирует его в основной каталог.

    while True:
        file_path = input("путь: ")
        path = Path(file_path)
        if not path.is_file():
            print("! по указанному пути отсутствует необходимый файл !")
            continue

        copied_file_path = load_file(path)
        
        # Импортируем модуль из скопированного файла
        spec = spec_from_file_location("conf", copied_file_path)
        config_module = module_from_spec(spec)
        spec.loader.exec_module(config_module)
        
        return config_module

#>>> config_module = ask_for_file()
#путь: d:\student\2023.05.28\conf.py
#! по указанному пути отсутствует необходимый файл !

#путь: C:\Users\user\MkrtchjanK\2024.12.14\data\conf.py
#>>>
#>>> config_module.defaults
#{'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
        