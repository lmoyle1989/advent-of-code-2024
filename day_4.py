f = open("day_4_input", "rt")

grid = []

for line in f:
    grid.append(list(line.strip('\n')))

m = len(grid)
n = len(grid[0])

directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

def isValid(r,c) -> bool:
    return r >= 0 and c >= 0 and r < m and c < n

def checkWord(r, c, grid) -> int:
    ans = 0
    for d in directions:
        word = ""
        for i in range(4):
            nr = r + (d[0] * i)
            nc = c + (d[1] * i)
            if isValid(nr,nc):
                word += grid[nr][nc]
        if word == "XMAS":
            ans += 1
    return ans

result = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == "X":
            result += checkWord(i, j, grid)

#print(result)

# pt 2

# patterns = [['M','.','M'],
#             ['.','A','.'],
#             ['S','.','S']]

coords = [(-1,-1), (-1, 1), (1,-1), (1,1)] #tl,tr,bl,br
patterns = set(["MMSS", "SMSM", "SSMM", "MSMS"])

ans2 = 0
for i in range(0, m ):
    for j in range(0, n):
        if grid[i][j] == "A":
            word = ""
            for d in coords:
                if isValid(i+d[0],j+d[1]):
                    word += grid[i+d[0]][j+d[1]]
            if word in patterns:
                ans2 += 1

print(ans2)