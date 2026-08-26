def selection_sort(nums: list[int]) -> list[int]:

    listLength = len(nums)


    for i in range(0, listLength):
        min = i
        for a in range(i + 1, listLength):
            if(nums[a] < nums[min]):
                min = a

        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp

    return nums

