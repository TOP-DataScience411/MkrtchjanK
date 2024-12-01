def deck():
    suits = ['черви', 'бубны', 'пики', 'трефы']
    values=list(range(2,11))+['валет', 'дама', 'король','туз']
    for suit in suits:
        for value in values: 
            yield (value, suit)

#>>> list(deck())[::13]
#[(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]