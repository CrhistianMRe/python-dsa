def quick_sort(nums, low, high):
    middle_index = 0  
    if(low < high):
        middle_index = partition(nums, low, high)
        quick_sort(nums, low, middle_index-1)
        quick_sort(nums, middle_index+1, high)
    

def partition(nums, low, high):
    pivot_element = nums[high] 
    i = low-1
    temp = None
    for j in range(low, high):
        if(nums[j] < pivot_element):
            i +=1
            temp = nums[i] 
            nums[i] = nums[j]
            nums[j] = temp
    right_index = i+1
    temp = pivot_element
    nums[high] = nums[right_index] 
    nums[right_index] = temp
    return right_index 






    
