def average_followers(nums):
    result = None
    if nums:
        average = 0
        for a in nums:
            average += a

        average = average/len(nums)
        result = average

    return result 







    
