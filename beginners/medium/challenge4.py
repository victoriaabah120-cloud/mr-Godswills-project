def balanced_brackets(text):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for t in text:
        if t in '([{':
            stack.append(char)

        elif t in ')]}':
            if not stack:
                return False

            last = stack.pop()

            if last != pairs[t]:
                return False

    return len(stack) == 0
