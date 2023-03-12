def findValidSplit(nums):
    new_nums = []
    def products(nums):
        z = 1
        for i in range(0,len(nums)):
            z *= nums[i]
        return z

    for i in range(0,len(nums)):
        new_nums.append(nums[i])
        nums.pop(i) 
        x = products(nums), products(new_nums)
        print(x)
    return 0

nums = [1,2,3,4]
x= findValidSplit(nums)
print(x)
