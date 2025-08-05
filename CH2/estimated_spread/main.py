def get_estimated_spread(audiences_followers):
    estimated_spread = 0
    if audiences_followers:
        sum = 0
        num_followers = len(audiences_followers)

        for i in audiences_followers:
            sum += i

        average_audience_followers = sum/num_followers

        estimated_spread = average_audience_followers *(num_followers ** 1.2)
    return estimated_spread






