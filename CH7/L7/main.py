from stack import Stack


def is_balanced(input_str: str) -> bool:
    stack = Stack()

    for i in input_str:
        if (i == "("):
            stack.push(i)
        elif (i == ")" and stack.size() == 0):
            stack.push(i)
        else:
            stack.pop()

    return stack.size() == 0




