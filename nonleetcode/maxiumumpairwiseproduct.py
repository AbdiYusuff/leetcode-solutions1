# def max_product(nums, n):
#     # if (n < 2):
#     #     print('No pairs exist')
#     #     return
#     # a = nums[0]; b = nums[1]

#     # for i in range(0, n):
#     #     for j in range(i+1, n):
#     #         if (nums[i]*nums[j]) > a * b:
#     #             a = nums[i]; b = nums[j]
#     # print("Max Product: ", a, " ", b)
#     # 
# nums = [1,2,3,4]
# max_product(nums, 4)

def maxProduct(nums): 
    n = len(nums)
    min1 = nums[0]
    min2 = float('inf')
    max1 = nums[0]
    max2 = -float('inf')

    for i in range(1,n):
        if nums[i] <= min1:
            min2 = min1
            min1 = nums[i]
        elif nums[i] <= min2:
            min2 = nums[i]

        if nums[i] >= max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i] > max2:
            max2 = nums[i]
    if min1*min2 > max1*max2:
        return min1*min2
    return max1*max2
nums = [10,2,5,2]
ans = maxProduct(nums)
print(ans)





