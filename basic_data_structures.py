# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def find_mismatch(text):

    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i+1))
            pass

        if next in ")]}":
            # Process closing bracket
            if len(opening_brackets_stack) == 0:
                return print(i+1)
            else:
                top = opening_brackets_stack.pop()
                if (top.char == '[' and next != ']') or (top.char == '{' and next != '}') or (top.char == '(' and next != ')'):
                    return print(i+1)

    if len(opening_brackets_stack) == 0:
        return print('Success')
    else:
        return print(opening_brackets_stack[0][1])


def main():
    text = input()
    find_mismatch(text)


if __name__ == "__main__":
    main()
    
    
