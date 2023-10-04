def topKFrequent(nums):
    nums_freq = {}
    for num in nums:
        if num in nums_freq:
            nums_freq[num] += 1
        else: 
            nums_freq[num] = 1
    print(nums_freq)
    res1 = max(nums_freq.keys())
    print(res1)

nums = [1,1,1,2,2,3]
res = topKFrequent(nums)


    
    
