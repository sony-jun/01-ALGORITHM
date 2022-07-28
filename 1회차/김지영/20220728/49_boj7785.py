log = int(input())
log_ = {}
for line in range(log):
    name, state = input().split()
    log_[name] = state

# print(log_)
k = [k for k,v in log_.items() if v == 'enter']
# 사전의 역순
k = sorted(k)
for i in k[::1]:
    print(i)