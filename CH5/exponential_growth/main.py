def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    result = []

    currentGrowthValue = n
    result.append(n)

    for i in range(0, days):
        currentGrowthValue = currentGrowthValue * factor
        result.append(currentGrowthValue)


    return result
