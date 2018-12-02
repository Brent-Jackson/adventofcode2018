fname = "input.txt"

with open(fname) as f:
    lines = f.readlines()

sum = 0
for line in lines:
    sum += int(line.strip())
    print("line: " + line.strip() + " \t sum: " + str(sum))

print("q1 final sum:",sum)



seen_sums = set()
sum = 0
iterations = 0
done = False

while iterations < 1000 and not done:
    for line in lines:
        sum += int(line.strip())
        # print("line: " + line.strip() + " \t sum: " + str(sum))
        if sum not in seen_sums:
            seen_sums.add(sum)
        else:
            print("first duplicated sum: ",sum)
            done = True
            break
    iterations += 1
    print("ITERATION",iterations)

print("Done")
