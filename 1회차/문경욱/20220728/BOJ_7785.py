N = int(input())

people_ = []
# 이름과 출입을 입력 받음
for _ in range(N):
    name, entry = map(str, input().split())
    # entry가 enter면 people에 추가, leave면 people에서 삭제
    if entry == 'enter':
        people_.append(name)
    if entry == 'leave':
        people_.remove(name)


# 사전 역순으로 정렬
people_.sort(reverse=True)

for person in people_:
    print(person)