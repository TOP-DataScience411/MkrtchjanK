a=list(map(int, input().split()))
b=list(map(int, input().split()))

for i in range (len(a)-len(b)+1):
    if b==a[i:i+len(b)]:
        print('да')
        break
else:
    print ('нет')
    
#1 2 3 4
#1 2
#да

#1 2 3 4
#2 4
#нет
