def threeSum(nums):
    
    result = enumerate(nums)
    print(result)
    my_dict = {}
    for i, element in enumerate(nums):
        my_dict[element] = i
    print(my_dict)
    # for j in range(len(nums)):
    #     for k in range(len(nums)):
    #         if (nums[j]+nums[k])*-1 in my_dict:
    #             return nums[i], nums[j], nums[k]
nums = [-1,0,1,2,-1,-4]   
res = threeSum(nums)
print(res)
