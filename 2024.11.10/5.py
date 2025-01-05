# Функция вычисляет медиану, среднее арифметическое, среднее геометрическое и среднее гармоническое значения для заданных чисел
from math import prod
def central_tendency(a: float, b: float, *nums: float) -> dict[str, float]:
    total={}
    numbers=[a,b]+list(nums)
    s_nums=sorted(numbers)
    n=len(s_nums)
    if n%2!=1:
        middle_index=n//2
        total['median']=(s_nums[middle_index-1]+s_nums[middle_index])/2
    else:
        total['median']=s_nums[n//2]
    total['arithmetic']=sum(s_nums)/n
    total['geometric']=prod(numbers)**(1/n)
    total['harmonic']=n/ sum(1 / num for num in s_nums)
    return total
    
#>>> central_tendency(1, 2, 3, 4)
#{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.92}
    
#>>> sample = [1, 2, 3, 4, 5] 
#>>> central_tendency(*sample)
#{'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
