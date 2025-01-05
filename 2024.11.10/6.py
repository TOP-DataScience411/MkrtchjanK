# Функция вычисляет длину недостающей стороны прямоугольного треугольника
from math import sqrt
def orth_triangle(cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    sides = [cathetus1, cathetus2, hypotenuse]
   
    if sides.count(0) != 1:
        return None
    
    if hypotenuse > 0 and (cathetus1 <= 0 and cathetus2 <= 0 or (cathetus1 > hypotenuse or cathetus2 > hypotenuse)):
        return None
    if hypotenuse > 0:
        if cathetus1 > 0:
            return sqrt(hypotenuse**2 - cathetus1**2)
        else:
            return sqrt(hypotenuse**2 - cathetus2**2)
    else:
        return sqrt(cathetus1**2 + cathetus2**2)

#>>> orth_triangle(cathetus1=3, hypotenuse=5)
#4.0 
#>>> orth_triangle(cathetus1=8, cathetus2=15)
#17.0 
#>>> orth_triangle(cathetus2=9, hypotenuse=3)
#None
