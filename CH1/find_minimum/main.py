def find_minimum(nums):
    minimum = None;
    if nums:
        minimum = float("inf")
        for i in nums:
            if i <= minimum:
                minimum = i;


    return minimum

