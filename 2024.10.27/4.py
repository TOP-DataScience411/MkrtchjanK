# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имена a, h, m, l ничего не говорят о том, какие значения ассоциированы с данными переменными — вместо них стоило назвать переменные number, digit1, digit2, digit3
a=int(input())
h=a//100
# ИСПРАВИТЬ: избыточное количество вычислений, можно проще
m=(a-h*100)//10
l=a-h*100-m*10
print(f"Сумма цифр = {h+m+l} \nПроизведение цифр = {h*m*l}")


#Сумма цифр = 9
#Произведение цифр = 27


# ИТОГ: доработать — 3/4

