

def merge_sort(nums):
    if(len(nums) < 2):
        return nums

    first_half = []
    second_half = []

    elements = int(len(nums)/ 2)

    for value in range(0, elements, 1):
        first_half.append(nums[value])
    for value in range(elements, len(nums), 1):
        second_half.append(nums[value])

    sorted_left_side = merge_sort(first_half)
    sorted_right_side = merge_sort(second_half)

    return merge(sorted_left_side, sorted_right_side) 

def merge(first, second):
    list = []
    i = 0
    j = 0
    print("left", len(first))
    print("right", len(second))
    first_length = (len(first))
    second_length = (len(second))
    while(i < first_length and j < second_length):
        print(j)
        if(first[i] <= second[j]):
            list.append(first[i])
            i += 1
        else:
            list.append(second[j])
            j += 1
    while(i < first_length):
        list.append(first[i])
        i += 1
    while(j < second_length):
        list.append(second[j])
        j += 1 
    return list;
            


        
        


