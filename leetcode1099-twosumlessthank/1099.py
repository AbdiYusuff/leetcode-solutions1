def twoSumLessThanK(nums, k):
    nums.sort()
    l, r = 0, len(nums)-1
    max_so_far = -1
    while l<r:
        print("before if statement")
        currSum = nums[r]+nums[l]
        if currSum >= k:
            r -= 1
        else:
            max_so_far = max(max_so_far, currSum)
            l += 1
        print("after else")
    return max_so_far

    # n = len(nums)
    # result = -1
    # for i in range(n):
    #     for j in range(i+1,n):
    #         currSum = nums[i]+nums[j]
    #         if currSum > result and currSum < k:
    #                 result = currSum
    #     return result
# nums = [10,20,30] 
# k = 15
nums = [34,23,1,24,75,33,54,8]
k = 60
res = twoSumLessThanK(nums, k)
print(res)