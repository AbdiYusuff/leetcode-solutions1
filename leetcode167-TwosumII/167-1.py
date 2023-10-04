def two_sum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i]+nums[j] == target:
    #             return i, j
            
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i 
        print(numMap)  

nums = [11,15,2,7] 
target = 9

# nums = [3,2,4]
# target = 6

results = two_sum(nums, target)
print(results)


