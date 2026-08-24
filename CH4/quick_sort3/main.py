def quick_sort(nums: list[int], low: int, high: int) -> None:
    if(low < high):
        middleIndex = partition(nums, low, high)

        quick_sort(nums, low, middleIndex - 1)
        quick_sort(nums, middleIndex + 1, high)


def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if(nums[j] < pivot):
            i += 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

    temp = nums[i + 1] 
    nums[i + 1] = nums[high]
    nums[high] = temp

    return i + 1



