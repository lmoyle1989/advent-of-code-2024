import re

f = open("day_3_input", "rt")
text = f.read()
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

nums = []
for match in matches:
    str_nums = re.findall(r"\d{1,3}", match)
    nums.append(list(map(int,str_nums)))

ans = []
for num in nums:
    ans.append(num[0] * num[1])

pt_1_ans = sum(ans)

santext = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", text)

test = []
cur = 1
pt_2_ans = []
for x in santext:
    if x == "don't()":
        cur = 0
    elif x == "do()":
        cur = 1 
    else:
        if cur == 1:
            nums = re.findall(r"\d{1,3}", x)
            pt_2_ans.append(int(nums[0]) * int(nums[1]))

print(sum(pt_2_ans))


f.close()