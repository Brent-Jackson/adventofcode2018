
lengths = {}

for i in range(ord('a'),ord('z')+1):
    omit = chr(i)

    with open('input.txt') as f:
        stack = []
        while True:
            c = f.read(1)
            if c.lower() == omit:
                continue
            if c is None or len(c) == 0:
                break
            if len(stack) > 0 and stack[-1] != c and (stack[-1].lower() == c.lower()):
                _ = stack.pop()
            else:
                stack.append(c)
    lengths[omit] = len(stack)

shortest = min(lengths, key=lengths.get)
print("Shortest polymer: {} ({} chars)".format(shortest,lengths[shortest]))

            
