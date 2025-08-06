def does_name_exist(first_names, last_names, full_name):
    result = False 
    for first in first_names:
        for last in last_names:
            possible = first + " " + last
            if full_name == possible:
                result = True 
                
    return result


