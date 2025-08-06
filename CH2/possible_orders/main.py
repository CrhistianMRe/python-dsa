def num_possible_orders(num_posts):
    sum = 1
    for i in range(num_posts+1):
        if i !=0:  
            sum *= i

    return sum
