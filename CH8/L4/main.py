from queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    username = user[0]
    action = user[1]

    if(action == "leave"):
        queue.search_and_remove(username)
    if(action == "join"):
        queue.push(username)

    if(queue.size() > 3):
        firstUser = queue.pop()
        secondUser = queue.pop()
        return firstUser + " matched " + secondUser + "!"
    else:
        return "No match found"


