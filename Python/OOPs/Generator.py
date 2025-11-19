def my_gen():
    
    n=1
    while(n<=10):
        sq=n*n
        yield sq
        n+=1

x=my_gen()

print(x)
# for i in x:
#     print(i)
# 3
# next(g)  # Raises StopIteration
