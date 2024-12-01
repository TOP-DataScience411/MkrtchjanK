def product(nums):
    if not nums:
        return 1.0
    else:
        first, *rest=nums
        return float(first)*abs(product(rest))
#>>> product(range(10, 60, 10))
#12000000.0
#>>> product((0.12, 0.05, -0.09, 0.0, 0.21))
#0.0