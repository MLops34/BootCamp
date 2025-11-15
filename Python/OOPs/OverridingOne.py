class Calculator:
   
    def sum(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif (a!=None and b!=None):
            s=b+a
        else:
            s=a
        return s

c=Calculator()
print(c.sum(5,8))
print(c.sum(2,6))