def average_followers(nums: list[int]) -> float | None:
    listLength = len(nums)

    totalSum = 0

    for i in nums:
        totalSum += i

    return totalSum / listLength


