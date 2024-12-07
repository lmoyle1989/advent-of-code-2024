f = open("day_7_input", "rt")

answers = []
nums= []

for line in f:
    x = line.strip('\n').split()
    answers.append(int(x[0].strip(":")))
    nums.append(list(map(int,x[1:])))

def validEq(ans, nums, i, cur) -> bool:
    if cur > ans:
        return False
    if i == len(nums):
        return cur == ans
    else:
        plus = cur + nums[i]
        mult = cur * nums[i]
        concat = int(str(cur) + str(nums[i]))
        return  validEq(ans, nums, i+1, plus) or \
                validEq(ans, nums, i+1, mult) or \
                validEq(ans, nums, i+1, concat)

validanswers = []
for i in range(len(answers)):
    if validEq(answers[i], nums[i], 1, nums[i][0]):
        validanswers.append(answers[i])

print(sum(validanswers))