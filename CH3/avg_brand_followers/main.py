def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    list_count = 0
    for list in all_handles:
        list_count += 1
        for string in list:
            if(string.find(brand_name) != -1): count += 1
    return count / list_count 




