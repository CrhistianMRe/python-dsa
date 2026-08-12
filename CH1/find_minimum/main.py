def find_minimum(nums: list[int]) -> float | None:
    if not nums: 
        return None
    minimum = float("inf")

    listLength = len(nums)

    for i in range(0, listLength):
        if nums[i] < minimum:
            minimum = nums[i]

    return minimum


