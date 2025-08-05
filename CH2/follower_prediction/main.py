def get_follower_prediction(follower_count, influencer_type, num_months):
    mult = None
    if influencer_type == "fitness":
        mult = 4
    elif influencer_type == "cosmetic":
        mult = 3 
    else:
        mult = 2

    return follower_count * (mult ** num_months) 

