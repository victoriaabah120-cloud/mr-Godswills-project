def balanced_brackets(text):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for t in text:
        if t in '([{':
            stack.append(t)

        elif t in ')]}':
            if not stack:
                return False

            last = stack.pop()

            if last != pairs[t]:
                return False

    return len(stack) == 0
print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))