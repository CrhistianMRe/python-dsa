def count_names(list_of_lists, target_name):
    count = 0 
    for list in list_of_lists:
        for string in list:
            if(string.find(target_name) != -1): count += 1
    return count

