def bs(a,t):
    l=0
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]<t:
            l=m+1
        else:
            h=m-1
    return -1

a=[2,3,4,5,8,9]
t=5
r=bs(a,t)

if r!=-1:
    print("Element found at index",r)
else:
    print("Element not found")
