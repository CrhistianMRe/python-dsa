def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count = 0
    for nameList in list_of_lists:
        for name in nameList:
            if name == target_name: count += 1
    return count
