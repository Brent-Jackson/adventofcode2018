
class Cell:
    def __init__(self,coord,id="-"):
        self.x = coord[0]
        self.y = coord[1]
        self.id = id

    def __str__(self):
        return self.id
        # return "{}: ({},{})".format(self.id,self.x,self.y)

def show(grid):
    xmin = min([i[0] for i in grid])
    xmax = max([i[0] for i in grid])
    ymin = min([i[1] for i in grid])
    ymax = max([i[1] for i in grid])
    print("upper-left: ({},{})\nbottom-right:({},{})".format(xmin,ymin,xmax,ymax))

    for y in range(ymin,ymax+1):
        print("".join([str(grid[x,y]) for x in range(xmin,xmax+1)]))

def solve(lines):

    letters=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    letters += [chr(i) for i in range(ord('a'),ord('z')+1)]
    letters.reverse()

    coords = []
    for i in range(len(lines)):
        coord = [int(x.strip()) for x in lines[i].split(",")]
        coords.append(coord)
    print(coords)


    left = min(coords, key=lambda i: i[0])
    right = max(coords, key=lambda i: i[0])
    top = min(coords, key=lambda i: i[1])
    bot = max(coords, key=lambda i: i[1])
    print("left:{} right:{} top:{} bot:{}".format(left,right,top,bot))
    

    xmin = min([i[0] for i in coords])
    xmax = max([i[0] for i in coords])
    ymin = min([i[1] for i in coords])
    ymax = max([i[1] for i in coords])
    grid_width = xmax - xmin
    grid_height = ymax - ymin
    print("grid: {}x{} ".format(grid_width,grid_height))


    grid = {}
    for y in range(ymin,ymax+1):
        for x in range(xmin,xmax+1):
            grid[(x,y)] = Cell([x,y],".")

    for c in coords:
        grid[(c[0],c[1])].id = letters.pop()

    show(grid)
    


def test():
    lines = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9"
    ]

    solve(lines)




with open("in.txt") as f:
    lines = f.readlines()

test()
# solve(lines)
