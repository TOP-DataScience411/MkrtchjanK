a=input()
if a.startswith('b'):
    a=a[1:]
if  a.startswith('0b'):
    a=a[2:]
if set(a)<={'0','1'}:
    print('да')
else:
    print('нет')
    
 #0101
 #да
 
 #1b0101
 #нет