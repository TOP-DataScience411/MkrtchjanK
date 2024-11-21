m=input()
if m.find('@')!=-1 and m.find ('.')!=-1 and m.rfind('.')>m.rfind('@'):
    print ('да')
else:
    print ('нет')

#sgd@ya.ru
#да

#abcde@fghij
#нет

