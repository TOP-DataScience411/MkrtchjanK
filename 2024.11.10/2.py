def taxi_cost(length: int, time: int = 0) -> int | None:
    if length<0 or time<0:
        return None
    price=80
    fine=80
    wait_time=time*3
    trip_price=length/150*6
    if length==0:
       return price+wait_time+fine
    total_price=price+trip_price+wait_time
    return round(total_price)
    
#>>>taxi_cost(1500)
#140
#>>>taxi_cost(2560)
#182
#>>>taxi_cost(0,5)
#175
#>>>taxi_cost(42130,8)
#1789
#>>>taxi_cost(-300)
#None