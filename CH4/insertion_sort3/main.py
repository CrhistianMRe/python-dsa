def insertion_sort(nums: list[int]) -> list[int]:
    listLength = len(nums)

    for i in range(1, listLength):
        j = i
        while(j > 0 and nums[j - 1] > nums[j]):
            temp = nums[j - 1]
            nums[j - 1] = nums[j]
            nums[j] = temp
            j -= 1

    return nums

