nums=[num for num in range(9)]
print(nums)

rotate=int(input("Enter the number of rotations: "))
rotate=rotate%len(nums)

for i in range(len(nums)):
    temp=nums[i]
    nums[i]=nums[(i+rotate)%len(nums)]
    nums[(i+rotate)%len(nums)]=temp
print(nums)
