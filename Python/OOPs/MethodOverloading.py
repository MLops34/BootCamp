# IN Python When we call add(),subtract(),print() it will call functions at the backend like define Below:
# __add__()
# __str__()
# Built IN Function when they call with built-in Datatypes they used to execute because they define like this __function__()

# x = 10
# y = 5

# print(x + y)          # calls x.__add__(y)
# print(x - y)          # calls x.__sub__(y)
# print(str(x))         # calls x.__str__()
# print(len([1, 2, 3])) # calls list.__len__([1,2,3])
 

#Built-in data types already have these special methods defined.
#For custom classes, we define them manually to make our objects behave like built-ins.

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1 + self.m2
        m2=other.m1+ other.m2
        s3=Student(m1,m2)

        return s3
    
    def __sub__(self,other):
        m1=self.m1-other.m1  # -300
        m2=self.m2-other.m2  # -200
        if(m1>m2):
            res=m2-m1
        else:
            res=m1-m2 # -300+200 
        
        return res
    
    def __gt__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+self.m2
        if(m1>m2):
            print(self.m1)
        else:
            print(self.m2)
    
    
s1=Student(100,200)

s2= Student(400,400)

s3=s1+s2

s3=s1-s2

print(s3)
# print(s3.m1,s3.m2)
