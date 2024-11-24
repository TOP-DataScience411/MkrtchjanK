def countable_nouns(number: int, noun: tuple[str, str, str]) -> str:
        if number%10==1 and number%100!=11:
            return noun[0]
        elif number%10 in [2,3,4] and not (number % 100 in [12, 13, 14]):
            return noun[1]
        else:
            return noun[2]

#>>> countable_nouns(1, ("год", "года", "лет")) 
#год
#>>> countable_nouns(2, ("год", "года", "лет"))
#года
#>>> countable_nouns(10, ("год", "года", "лет"))
#лет
#>>> countable_nouns(12, ("год", "года", "лет"))
#лет
#>>> countable_nouns(22, ("год", "года", "лет"))
#года