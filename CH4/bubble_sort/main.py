def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while(swapping):
        swapping = False
        for start in range(1, end):
            if(nums[start-1] > nums[start]): 
                temporal = nums[start-1]
                nums[start-1] = nums[start]
                nums[start] = temporal
                swapping = True
        end -= 1
    return nums



