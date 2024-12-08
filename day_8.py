f = open("day_8_input", "rt")

grid = []

for line in f:
    x = list(line.strip('\n'))
    grid.append(x)

m = len(grid)
n = len(grid[0])

all_ants = {}

for i in range(m):
    for j in range(n):
        if grid[i][j] != ".":
            if grid[i][j] not in all_ants:
                all_ants[grid[i][j]] = [(i,j)]
            else:
                all_ants[grid[i][j]].append((i,j))

def validNode(r, c):
    return r >= 0 and c >= 0 and r < m and c < n

def getAntinodes(a, b):
    rd = b[0] - a[0]
    cd = b[1] - a[1]
    node1 = (a[0] - rd, a[1] - cd)
    node2 = (b[0] + rd, b[1] + cd)
    return (node1, node2)

antinodes = set()

# for ant_type in all_ants:
#     ants = all_ants[ant_type]
#     for i in range(len(ants) - 1):
#         for j in range(i + 1, len(ants)):
#             n1, n2 = getAntinodes(ants[i], ants[j])
#             if validNode(n1[0], n1[1]):
#                 antinodes.add(n1)
#             if validNode(n2[0], n2[1]):
#                 antinodes.add(n2)

# print(len(antinodes))

# pt_2

def getAllAntinodes(a, b):
    nodes = set()
    nodes.add(a)
    nodes.add(b)
    rd = b[0] - a[0]
    cd = b[1] - a[1]
    node1 = (a[0] - rd, a[1] - cd)
    while validNode(node1[0], node1[1]):
        nodes.add(node1)
        node1 = (node1[0] - rd, node1[1] - cd)
    node2 = (b[0] + rd, b[1] + cd)
    while validNode(node2[0], node2[1]):
        nodes.add(node2)
        node2 = (node2[0] + rd, node2[1] + cd)
    return list(nodes)

antinodes2 = set()

for ant_type in all_ants:
    ants = all_ants[ant_type]
    for i in range(len(ants) - 1):
        for j in range(i + 1, len(ants)):
            nodes = getAllAntinodes(ants[i], ants[j])
            for node in nodes:
                antinodes2.add(node)

print(len(antinodes2))