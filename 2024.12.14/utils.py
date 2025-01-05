from pathlib import Path
from shutil import copy2

def load_file(file_path: Path) -> Path:

    #Копирует файл по переданному пути в основной каталог.

    destination_path = Path("conf.py")  # Имя файла, в который будет скопирован файл
    copy2(file_path, destination_path)
    return destination_path