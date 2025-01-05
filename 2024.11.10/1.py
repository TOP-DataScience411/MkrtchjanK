# Функция проверяет, является ли заданный пароль надежным, по определенным условиям
def strong_password(password):
    if len(password)<8:
        return False
        
    upper=False
    lower=False
    digit=0
    symbol=False
    
    for i in password:
        if i.isupper():
            upper=True
        elif i.islower():
            lower=True
        elif i.isdigit():
            digit+=1
        else:
            symbol=True
    if upper and lower and digit>2 and symbol:
        return True
    else:
        return False
        

#>>> strong_password('aP3:kD_l3')
#True
#>>> strong_password('password')
#False    
    



        
    
    
