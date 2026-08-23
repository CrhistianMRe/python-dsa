def merge_sort(nums: list[int]) -> list[int]:
    listLength = len(nums)

    if(listLength < 2): return nums

    firstHalfAmount = listLength // 2

    firstHalfList = []
    secondHalfList = []

    for i in range(0, firstHalfAmount): firstHalfList.append(nums[i])

    for a in range(firstHalfAmount, listLength): secondHalfList.append(nums[a])

    sortedLeftSide = merge_sort(firstHalfList)
    sortedRightSide = merge_sort(secondHalfList)

    return merge(sortedLeftSide, sortedRightSide)


def merge(first: list[int], second: list[int]) -> list[int]:
    resultList = []

    firstListLength = len(first)
    secondListLength = len(second)

    i = 0
    j = 0

    while(i < firstListLength and j < secondListLength):
        if(first[i] < second[j]):
            resultList.append(first[i])
            i += 1
        else:
            resultList.append(second[j])
            j += 1

    while(i < firstListLength):
        resultList.append(first[i])
        i += 1

    while(j < secondListLength):
        resultList.append(second[j])
        j += 1


    return resultList



