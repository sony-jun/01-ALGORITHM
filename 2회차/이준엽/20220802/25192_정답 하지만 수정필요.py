# n = int(input())
# log = []
# cnt = 0
# tmp = set()
# for i in range(n):
#     new = input()
#     log.append(new)
# for jud in log:
#     if jud == 'ENTER':
#         cnt+=len(tmp)
#         tmp = set()
#     else:
#         tmp.add(jud)
# cnt+=len(tmp)
# print(cnt)

n = int(input())
logs = [input() for i in range(n)]
judge = set()
gom = 0
for log in logs:
    if log == 'ENTER':
        gom+=len(judge)
        judge.clear()
    else:
        judge.add(log)
gom+=len(judge)
print(gom)

n = int(input())
logs = [input() for i in range(n)]
judg = set()
gom = 0

for log in logs:
    if log == 'ENTER':
        judg.clear()
    else:
        if log not in judg:
            judg.add(log)
            gom+=1