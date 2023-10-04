def threeSum(nums):
    numsMap = {}
    n = len(nums)
    nums.sort()
    for i in range(n):
        while nums[i] != nums[i+1]:
            
        for j in range(n):
            if nums[i]+nums[j]
        numsMap[nums[i]] = i
    print(numsMap)

nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(res)