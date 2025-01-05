# Функция вычисляет произведение чисел в списке
def product(nums):
    if not nums:
        return 1.0
    first, *rest=nums
    total=float(first)*product(rest)
    if total==0:
        return 0.0
    else:
        return total
    
#>>> product(range(10, 60, 10))
#12000000.0
#>>> product((0.12, 0.05, -0.09, 0.0, 0.21))
#0.0
