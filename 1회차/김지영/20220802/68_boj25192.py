# 곰곰티콘의 갯수
# enter는 새로운 사람 입장
# 이후 처음 등장하는 이름은 무조건 곰곰티콘
log_line = int(input())
log = set()
hi = 0
for i in range(log_line):
    state_name = input()
    if state_name == 'ENTER' and len(log) != 0 :
        hi += len(log) - 1
        log = set()
        # print(len(log),hi)
    log.add(state_name)
hi += len(log)-1
print(hi)