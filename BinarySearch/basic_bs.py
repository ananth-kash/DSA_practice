a=[12,34,44,55,66]
def binarysearch(start,end,c,ele):
    if start>end:
        return -1
    mid=(start+end)//2
    if(ele>c[mid]):
        return binarysearch(mid+1,end,c,ele)
    elif(ele<c[mid]):
        return binarysearch(start,mid-1,c,ele)
    elif(c[mid]==ele):
        return mid
    
d=binarysearch(0,len(a)-1,a,66)
print(d)
    

