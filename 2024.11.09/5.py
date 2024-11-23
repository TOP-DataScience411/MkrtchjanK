scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'}
a=input().upper().replace('Ё','Е')
count=0
for i in a:
    for scores,letters in scores_letters.items():
        if i in letters:
            count+=scores
print(count)

#синхрофазотрон
#29