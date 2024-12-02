all_answers = []

# pt 1
f = open("day_1_input", "rt")

l = []
r = []

for line in f:
    pair = line.split()
    l.append(int(pair[0]))
    r.append(int(pair[1]))

l.sort()
r.sort()
diff = []

for i in range(len(l)):
    diff.append(abs(l[i] - r[i]))

all_answers.append(sum(diff))

# pt 2
r_cnt = {}
for x in r:
    if x not in r_cnt:
        r_cnt[x] = 1
    else:
        r_cnt[x] += 1

similarity = []
for y in l:
    if y in r_cnt:
        similarity.append(r_cnt[y] * y)

all_answers.append(sum(similarity))

print(all_answers)