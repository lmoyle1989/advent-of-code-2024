f = open("day_9_input", "rt")

input = list(f.read().strip('\n'))

# ans = []
# nums = []

# idx = 0
# for i, c in enumerate(input):
#     if i % 2 == 0:
#         for x in range(int(c)):
#             nums.append(idx)
#             ans.append(idx)
#         idx += 1
#     else:
#         for y in range(int(c)):
#             ans.append(".")

# res = []
# size = len(nums)
# final = 0
# for i in range(size):
#     if ans[i] != ".":
#         res.append(ans[i])
#     else:
#         res.append(nums.pop())
#     final += res[i] * i

# print(final)

mem = []
blocks = []
free = []

idx = 0
for i, c in enumerate(input):
    if i % 2 == 0:
        blocks.append([int(c), idx, len(mem)]) #[size, id, blockidx]
        for x in range(int(c)):
            mem.append(idx)
        idx += 1
    else:
        free.append([int(c), len(mem)]) #[size, startidx]
        for y in range(int(c)):
            mem.append(".")

while blocks:
    block_size, block_val, block_idx = blocks.pop()
    for i, f in enumerate(free):
        space_size, space_idx = f
        if space_size >= block_size and space_idx < block_idx:
            for j in range(block_size):
                mem[space_idx + j], mem[block_idx + j] = mem[block_idx + j], mem[space_idx + j]
            free[i][0] = space_size - block_size
            free[i][1] = space_idx + block_size
            break

result = 0
for i in range(len(mem)):
    if mem[i] != ".":
        result += mem[i] * i

print(result)