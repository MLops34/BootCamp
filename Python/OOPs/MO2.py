class SmartAdder:
    def add(self,a,b):
        s=0
        if type(a)==type(b)==int:
            s=a+b
        elif type(a)==type(b)==str:
            s=a+b
        elif type(a)==type(b)==list:
            s=a+b
        else:
            return "HAHA"
        
        return s

x=SmartAdder()


print(x.add(3, 5))      
print(x.add("AI", "ML"))     
print(x.add([1, 2], [3, 4]))
print(x.add(5, "ML")) 