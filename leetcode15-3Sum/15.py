def threeSum(nums):
    numsMap = {}
    n = len(nums)
    for i in range(n):
        numsMap[nums[i]] = i
    print(numsMap)

nums = [1,2,3,4,5,6,7,8]
res = threeSum(nums)
print(res)