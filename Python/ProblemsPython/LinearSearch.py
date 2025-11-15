def ls(a,t):
    for i in range(len(a)):
        if a[i]==t:
            return i
    return -1

a=[5,3,8,4,2,9]
t=4
print(ls(a,t))
