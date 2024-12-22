from pathlib import Path

def list_files(path: str) -> tuple:
    
    # Преобразуем строку пути в объект Path
    directory = Path(path)
    
    # Проверяем, существует ли каталог
    if not directory.is_dir():
        return None
    
    # Получаем имена файлов в каталоге и возвращаем их в виде кортежа
    #return: Кортеж с именами файлов или None, если каталог не существует.
   
    files = [file.name for file in directory.iterdir() if file.is_file()]
    return tuple(files) if files else None
    
print(list_files(r'C:\Users\user\MkrtchjanK\2024.12.14\data'))
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
    
 