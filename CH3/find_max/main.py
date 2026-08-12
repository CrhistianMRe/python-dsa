def find_max(nums: list[float]) -> float:

    max = float("-inf")

    for i in nums:
        if i > max:
            max = i

    return max

    

