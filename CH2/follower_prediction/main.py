def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    result = 0
    if influencer_type == "fitness":
        result = follower_count * 4 ** num_months

    elif influencer_type == "cosmetic":
        result = follower_count * 3 ** num_months
    else:
        result = follower_count * 2 ** num_months

    return result


