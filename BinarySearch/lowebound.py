a=[3,5,8,15,19]
b=[1,2,2,3]

def bs(start,end,arr,x):
    mid=(start+end)//2
    if(start>end):
        return -2
    if (arr[mid]==x):
        return mid+1
    elif(x>arr[mid]):
        return bs(mid+1,end,arr,x)
    else:
        return bs(start,mid-1,arr,x)
    

d=bs(0,len(a)-1,a,8)
e=bs(0,len(a)-1,b,2)
print(d)
print(e)