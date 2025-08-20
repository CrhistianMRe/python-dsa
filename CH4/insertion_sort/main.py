def insertion_sort(nums):
    for value in range(1, len(nums)):
        j = value
        temp = None 
        while(j > 0 and (nums[j-1] > nums[j])):
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            j -= 1
    return nums





