from functools import cmp_to_key

f = open("day_5_input", "rt")

rules = []
updates = []

for line in f:
    if "|" in line:
        rules.append(line.strip('\n'))
    elif len(line) > 1:
        updates.append(line.strip('\n').split(","))

rm = {}

for rule in rules:
    nums = rule.split("|")
    if nums[0] not in rm:
        rm[nums[0]] = set()
    if nums[1] not in rm:
        rm[nums[1]] = set()
    rm[nums[0]].add(nums[1])

valid_updates = []
invalid_updates = []
for update in updates:
    valid = True
    for i, cur in enumerate(update):
        for j in range(0, i):
            if update[j] in rm[cur]:
                valid = False
    if valid:
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

mids = []
for u in valid_updates:
    mids.append(u[len(u) // 2])

ans = map(int, mids)
# print(sum(ans))

def mycompare(a, b) -> int:
    if b in rm[a]:
        return -1
    elif a in rm[b]:
        return 1
    else:
        return 0
    
pt2ans = []
for invalid_update in invalid_updates:
    invalid_update.sort(key=cmp_to_key(mycompare))
    pt2ans.append(invalid_update[len(invalid_update) // 2])

intans = map(int, pt2ans)

print(sum(list(intans)))

f.close()