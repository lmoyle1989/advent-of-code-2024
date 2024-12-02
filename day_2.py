f = open("day_2_input", "rt")

reports = []

for line in f:
    reports.append(list(map(int, line.split())))

def validReport(report):
    if report != sorted(report) and report != sorted(report, reverse = True):
        return False
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff > 3 or diff == 0:
            return False
    return True
    
ans = []

for report in reports:
    if validReport(report):
        ans.append(1)
    else:
        for i in range(len(report)):
            temp = 0
            if validReport(report[:i] + report[i+1:]):
                temp = 1
                break
        ans.append(temp)

print(sum(ans))