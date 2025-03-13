a=[10,22,12,34,3,33]
#bubble sort
n=len(a)-1
for i in range(n,0,-1):
    for j in range(i):
        if(a[j]>a[j+1]):
            a[j], a[j+1]=a[j+1],a[j]

print(a)