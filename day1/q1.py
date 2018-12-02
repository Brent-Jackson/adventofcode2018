fname = "input.txt"

with open(fname) as f:
    lines = f.readlines()

sum = 0
for line in lines:
    sum += int(line.strip())
    print("line: " + line.strip() + " \t sum: " + str(sum))

print("q1 final sum:",sum)