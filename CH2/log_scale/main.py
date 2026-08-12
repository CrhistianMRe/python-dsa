import math


def log_scale(data: list[float], base: float) -> list[float]:
    resultList = []

    for num in data:
        resultList.append(math.log(num, base))
    
    return resultList


