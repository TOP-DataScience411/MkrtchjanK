b=list()
while True:
    a = input()
    if a!='':
        b.append(a)
    else:
        break
        
if  len(b)==1:
    print(b)
elif len(b)==2:
    print(f'{b[0]} и {b[1]}')
else:
    print(f'{','.join(b[:-1])} и {b[-1]}')

#яблоко
#яблоко

#яблоко
#груша
#яблоко и груша

#яблоко
#груша
#апельсин
#яблоко,груша и апельсин
    