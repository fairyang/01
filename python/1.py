'''n=eval(input())
a=int((n+1)/2)
for i in range(1,a+1,1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    for q in range (a-i):
        print(" ",end="")
    print()'''

'''a=eval(input())
for i in range((a+1)//2):
    b="*"*(2*i+1)
    b=str(b)
    print(b.center(a," "))'''
n=eval(input())
a=n.split('-')
print(a[0]+"+"+ls[-1])
