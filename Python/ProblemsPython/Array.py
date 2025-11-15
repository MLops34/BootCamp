nums=[1,2,3,4,5,6]
start=0
end=len(nums)-1

while (start<end):
    temp=nums[start]
    nums[start]=nums[end]
    nums[end]=temp
    start+=1
    end-=1  
print(nums)


