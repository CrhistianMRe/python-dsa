import math 

def log_scale(data, base):
    list = []
    for i in data:
        list.append(math.log(i, base))
    return list
        

