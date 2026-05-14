from queue import Queue


def matchmake(queue, user):
    name = user[0]
    action = user[1]

    if(action == "leave"): queue.search_and_remove(name)

    if(action == "join"): queue.push(name)

    if(queue.size() > 3):
        return queue.pop() + " matched" + " " + queue.pop() + "!"
    else: return "No match found"




