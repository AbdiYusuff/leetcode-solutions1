def contains_duplicate(nums): 
    # nums_dict = {}
    # for i in range(len(nums)):
    #     if nums[i] in nums_dict:
    #         return True
    #     nums_dict[i] = nums[i]
    #     print(nums_dict)
    # return False



    # seen = {}
    # for num in nums:
    #         if num in seen and seen[num] >= 1:
    #             return True
    #         seen[num] = seen.get(num, 0) + 1
    #         print(seen)
    # return False

    seen = set()
    for num in nums:
            print(seen)
            if num in seen:
                return True
            seen.add(num)
            
    return False
nums = [1,2,3,4,5,6]
result = contains_duplicate(nums)
print(result)