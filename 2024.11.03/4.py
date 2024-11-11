n=int(input())
sum=0
for i in range (10**(n-1), 10**n):
    for j in range (2, int(i**0.5+1)):
        if i%j==0:
            break
    else:
            sum+=1
print(sum)

#3
#143