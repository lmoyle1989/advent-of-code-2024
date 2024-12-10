f = open("day_10_input", "rt")

grid = []

for line in f:
    x = list(map(int, line.strip('\n')))
    grid.append(x)

m = len(grid)
n = len(grid[0])
dirs = [(1,0),(0,-1),(-1,0),(0,1)]

def valid(r,c):
    return r >= 0 and c >= 0 and r < m and c < n

def dfs(r,c,cur):
    if grid[r][c] == 9: # and (r,c) not in visited9:
        # visited9.add((r,c))
        score[-1] += 1
    else:
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if valid(nr,nc):
                if grid[nr][nc] == (cur + 1):
                    dfs(nr,nc,cur+1)

score = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            # visited9 = set()
            score.append(0)
            dfs(i,j,0)

print(sum(score))
