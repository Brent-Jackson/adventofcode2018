
# YyLlXxYKkbNnQqBFfxXbyYWw
with open('input.txt') as f:

    stack = []

    i = 0
    while i < 100000:
        c = f.read(1)
        if c is None or len(c) == 0:
            break
        if len(stack) > 0 and stack[-1] != c and (stack[-1].lower().upper() == c.lower().upper()):
            _ = stack.pop()
        else:
            stack.append(c)
        i += 1
    print("Final stack length: ",len(stack))

        
