def productExceptSelf(nums):
    # 1. Declere a new array of size len(nums)
    # 2. iterate through the nums list
    #     1.iterate through  nums list once again:
    #         1. for nums[i], return the product
    #         of all other nums except self. 
    n = len(nums)
    product = 1
    productArray  = []*n
    for i in range(1,n):
        for j in range(i,n):
            product *= nums[j]
    productArray[i] = product
    print(productArray)
    return productArray
nums = [1,2,3,4]
result = productExceptSelf(nums)
print(result)