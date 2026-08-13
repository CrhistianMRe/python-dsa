def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    handle_amount = 0

    parentListLength = len(all_handles)

    for i in range(0, parentListLength):
        subList = all_handles[i]
        subListLength = len(subList)
        for a in range(0, subListLength):
            if brand_name in subList[a]:
                handle_amount += 1


    print(parentListLength)

    return handle_amount / parentListLength
            




