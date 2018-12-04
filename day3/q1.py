import re

class Claim:
    def __init__(self,str):
        regex = ".*@\s+(\d+),(\d+):\s+(\d+)x(\d+)"
        match = re.match(regex,str)
        self.x = int(match.group(1))
        self.y = int(match.group(2))
        self.w = int(match.group(3))
        self.h = int(match.group(4))

    def __str__(self):
        return "{},{} {}x{}".format(self.x, self.y, self.w, self.h)


def show(grid):
    for y in grid:
        print(" ".join(str(x) for x in y))



def solve(lines):

    x_max = 0
    y_max = 0

    claims = [Claim(line) for line in lines]
    for claim in claims:
        if claim.x + claim.w > x_max:
            x_max = claim.x + claim.w
        if claim.y + claim.h > y_max:
            y_max = claim.y + claim.h
    grid = [[0 for x in range(x_max)] for y in range(y_max)]

    print("x_max:",x_max)
    print("y_max:",y_max)

    total_overlaps = 0

    for claim in claims:
        for h in range(claim.h):
            for w in range(claim.w):
                grid[claim.y+h][claim.x+w] += 1
                if grid[claim.y+h][claim.x+w] == 2:
                    total_overlaps += 1
    

    # grid[y][x] notation 
    # show(grid)

    return total_overlaps

        
def test():
    claims = [
        "#1 @ 0,0: 2x2",
        "#2 @ 1,1: 3x4",
        "#3 @ 2,2: 2x2",
        "#4 @ 0,1: 3x6"        
    ]

    print(solve(claims))


fname = "input.txt"

with open(fname) as f:
    lines = f.readlines()


# test()
print("Total overlapped squares:",solve(lines))


