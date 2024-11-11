n=[]
while True:
    a=int(input())
    if a%7!=0:
        break
    n.append(a)
print(n[::-1])

#7
#7
#14
#21
#13
#[21, 14, 7, 7]
