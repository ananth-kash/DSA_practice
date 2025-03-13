a=[10,22,12,34,3,33]
n=len(a)
for i in range(n):
    smallest_index=i
    for j in range(i+1,n):
        if(a[j]<a[smallest_index]):
            smallest_index=j
    a[i],a[smallest_index]=a[smallest_index],a[i]



print(a)