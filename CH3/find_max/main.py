def find_max(nums):
    max = float("-inf") 
    for i in nums:
        if i >= max:
            max = i
    return max


