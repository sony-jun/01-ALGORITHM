# pc가 1~100번까지..
# 손님이 번호를 말하면 앉아, 사람있으면 거절, 
# 거절 당한 사람은?
# input = 손님 수 N
#           손님이 들어오는 순서대로 손님자리 input
from collections import Counter
n = int(input())
cstm = list(map(int,input().split()))
cnt = Counter(cstm)
reject = 0
for k,v in cnt.items():
    if v > 1:
        reject += v-1
print(reject)

