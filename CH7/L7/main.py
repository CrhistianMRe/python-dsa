from stack import Stack


def is_balanced(input_str):
    stack = Stack()

    for c in input_str:

        if(c == ")"):
            tempResult = stack.pop()
            if(not tempResult): return False;

        if(c == "("):
           stack.push(c)
    return stack.size() == 0







