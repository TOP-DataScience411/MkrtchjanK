import csv
from pathlib import Path

class CountableNouns:
    #Класс для работы с файловой базой существительных.

    db_path = Path(r'C:\Users\user\MkrtchjanK\2024.12.15/words.csv')  
    words:dict[str, tuple[str, str]] = {}

    with db_path.open('r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            words[row[0]] = tuple(row[1:])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
    #Возвращает согласованное с числом существительное.
        if word in cls.words:
            if number % 10 == 1 and number % 100 != 11:
                return word  
            elif number % 10 in (2, 3, 4) and not (number % 100 in (12, 13, 14)):
                return cls.words[word][0]
            else:
                return cls.words[word][1] 
        else:
            print(f'Существительное "{word}" отсутствует в базе.')
            cls.save_words(word)
            return word

    @classmethod
    def save_words(cls, word1: str = None) -> None:
    #Запрашивает у пользователя слова для согласования и сохраняет их в базе.
        if word1:
            word2 = input('Введите слово, согласующееся с числительным "два": ')
            word5 = input('Введите слово, согласующееся с числительным "пять": ')
            cls.words[word1] = (word2, word5)
        else:
            word1 = input('Введите слово, согласующееся с числительным "один": ')
            word2 = input('Введите слово, согласующееся с числительным "два": ')
            word5 = input('Введите слово, согласующееся с числительным "пять": ')
            cls.words[word1] = (word2, word5)
            

    #Добавляет новые слова в файл.
        with cls.db_path.open('a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([word1, word2, word5])

#>>> CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
#>>> 
#>>> CountableNouns.pick(22, 'год')
#'года'
#>>> CountableNouns.pick(365, 'день')
#'дней'
#>>> 
#>>> CountableNouns.pick(21, 'попугай')
#'попугай'
#>>> CountableNouns.pick(22, 'попугай')
#существительное "попугай" отсутствует в базе
#введите слово, согласующееся с числительным "два": попугая
#введите слово, согласующееся с числительным "пять": попугаев
#>>>
#>>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
#>>>
#>>> CountableNouns.save_words()
#введите слово, согласующееся с числительным "один": капля
#введите слово, согласующееся с числительным "два": капли
#введите слово, согласующееся с числительным "пять": капель
#>>>
#>>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
#год,года,лет
#месяц,месяца,месяцев
#день,дня,дней
#попугай,попугая,попугаев
#капля,капли,капель

