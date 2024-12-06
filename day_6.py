f = open("day_6_test", "rt")

grid = []

for line in f:
    grid.append(list(line.strip('\n')))

for row in grid:
    print(row)