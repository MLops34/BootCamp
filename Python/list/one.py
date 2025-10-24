#List Comprehension
#List comprehension is a concise way to create lists in Python. It consists of brackets containing an

num=[]

for i in range(20):
    num.append(i)

# print(num)

ex=[num for num in range(20) if num==3]
# print(ex)

double=[[i,j] for i in range(10) for j in range(10) if i==j]
# print(double)
''' Slicing in List '''

cards=["Jack","Queen","King","Ace"]
# print(cards[0:2])
# print(cards[::])
# print(cards[::-1])

''' BUILT IN FUNCTIONS '''

cards.remove("Queen")
#print(cards)

nums=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(nums)):
    for j in range(i,len(nums)):
        temp=nums[i][j]
        nums[i][j]=nums[j][i]
        nums[j][i]=temp

for i in range(len(nums)):
    nums[i].reverse()
        
# print(nums)

#---reverse a list without using inbuilt function

nums=[1,2,3,4,5,6]
start=0
end=len(nums)-1

while (start<end):
    temp=nums[start]
    nums[start]=nums[end]
    nums[end]=temp
    start+=1
    end-=1  
# print(nums)

lst1=[1,2,2,3,4,5,5,6,7,9]
lst2=[2,3,4,5,6,7,8,10]
res=[num for num in lst1 if num not in lst2]
print(res)



### Accessing List Elements

fruits=["apple","banana","cherry","kiwi","gauva"]

print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])


print(fruits[1:])
print(fruits[1:3])

## List Methods

fruits.append("orange") ## Add an item to the end
print(fruits)

## Remove and return the last element
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)



## Slicing List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])