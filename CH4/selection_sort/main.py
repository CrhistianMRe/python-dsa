def selection_sort(nums):
    for i in range(0,len(nums)):
        smallest_idx = i
        for a in range(i+1, len(nums)):
            if(nums[a] < nums[smallest_idx]):
                smallest_idx = a
        temp = nums[i]
        nums[i] = nums[smallest_idx]
        nums[smallest_idx] = temp
    return nums;


