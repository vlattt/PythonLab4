a=[1,4,2,63,22,64,74,21,77,8]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)
