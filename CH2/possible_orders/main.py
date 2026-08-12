def num_possible_orders(num_posts: int) -> int:
    total = 1

    for i in range(num_posts, 1, -1):
        total *= i 

    return total


