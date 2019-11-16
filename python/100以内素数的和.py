s=0
for i in range(1,100):
    for j in range (1,i):
        if i%j==0 :
            if j==i:
                s=s+i
            else:
                break
print(s)           
