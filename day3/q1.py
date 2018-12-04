import re

class Claim:
    def __init__(self,str):
        regex = "#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)"
        match = re.match(regex,str)
        self.id = int(match.group(1))
        self.x = int(match.group(2))
        self.y = int(match.group(3))
        self.w = int(match.group(4))
        self.h = int(match.group(5))

    def __str__(self):
        return "#{} @ {},{} {}x{}".format(self.id, self.x, self.y, self.w, self.h)


def show(grid):
    for y in grid:
        print(" ".join(str(x) for x in y))



def solve_q1(lines):

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

    return total_overlaps, grid

def solve_q2(grid, lines):
    claims = [Claim(line) for line in lines]
    for claim in claims:
        print(claim)
        unoverlapped = True
        h = 0
        while h < claim.h and unoverlapped:
            w = 0
            while w < claim.w and unoverlapped:
                if grid[claim.y+h][claim.x+w] != 1:
                    unoverlapped = False
                    print("\toverlapped at {},{}".format(claim.x+w,claim.y+h))
                w += 1
            h += 1

        if unoverlapped:
            print("\tunoverlapped!")
            return claim
    return None


        
def test():
    claims = [
        "#1 @ 0,0: 2x2",
        "#2 @ 1,1: 3x4",
        "#3 @ 2,2: 2x2",
        "#4 @ 0,1: 3x6",
        "#5 @ 5,1: 2x2"      
    ]

    q1,grid = solve_q1(claims)
    show(grid)
    print("overlapped_squares:",q1)

    print("Unoverlapped_claim:",solve_q2(grid,claims))


fname = "input.txt"

with open(fname) as f:
    lines = f.readlines()


test()

q1, grid = solve_q1(lines)
print("Total overlapped squares:",q1)

q2 = solve_q2(grid, lines)
print("unoverlapped claim:",q2)


