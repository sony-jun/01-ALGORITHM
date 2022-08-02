# 25192번 인사성 밝은 곰곰이

# 받을 데이터의 수
N = int(input())
# 곰곰인사하는 사람을 넣을겁니다!
count = set()
# enter 할때마다 count 되는 사람 수를 전부 합할겁니다!
res = 0

for _ in range(N):
    # 입장을 나타내는 ENTER, 혹은 채팅을 입력한 유저의 닉네임이 문자열로 주어진다.
    sta = input()
    if sta == 'ENTER':
        res += len(count)
        count.clear()
    else:
        count.add(sta)

res += len(count)
print(res)