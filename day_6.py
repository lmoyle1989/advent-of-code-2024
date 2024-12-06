f = open("day_6_input", "rt")

grid = []

for line in f:
    grid.append(list(line.strip('\n')))

m = len(grid)
n = len(grid[0])

curp = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            curp = [i,j]

dirs = [(-1,0), (0,1), (1,0), (0,-1)]
curd = 0

def isValid(r,c) -> bool:
    return r >= 0 and c >= 0 and r < m and c < n

visited = set()

# pt 1

# while True:
#     r,c = curp
#     visited.add((r,c))
#     nr = r + dirs[curd][0]
#     nc = c + dirs[curd][1]
#     if isValid(nr, nc):
#         if grid[nr][nc] == "#":
#             curd = (curd + 1) % 4
#         else:
#             curp = [nr, nc]
#     else:
#         print(r,c)
#         break

# print(len(visited))

# pt 2

def patrol(curp, curd) -> int:
    visited2 = set()
    while True:
        r,c = curp
        if (r,c,curd) in visited2:
            return 1
        visited2.add((r,c,curd))
        nr = r + dirs[curd][0]
        nc = c + dirs[curd][1]
        if isValid(nr, nc):
            if grid[nr][nc] == "#":
                curd = (curd + 1) % 4
            else:
                curp = [nr, nc]
        else:          
            return 0
        
loop_count = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == ".":
            grid[i][j] = "#"
            loop_count += patrol(curp, curd)
            grid[i][j] = "."

print(loop_count)