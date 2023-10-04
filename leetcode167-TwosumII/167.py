def twoSum(nums, target):
    l, r = 0, len(nums)-1
    while l < r: 
        currSum = nums[l]+nums[r]

        if currSum < target:
            l =+ 1
        if currSum > target:
            r =- 1
        else: 
            return [l+1, r+1]
    return []

numbers = [2,7,11,15]
target = 9
res = twoSum(numbers,target)
print(res)