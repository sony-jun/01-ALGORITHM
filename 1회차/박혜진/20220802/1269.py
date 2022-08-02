# 시간 초과

# A의 원소 개수와 B의 원소의 개수 입력받기
A, B = map(int, input().split())

daeching = []
# A의 원소를 리스트로 입력받아 대칭 리스트에 저장
a = daeching.append(list(map(int, input().split())))

# B의 원소를 리스트로 입력받아 대칭 리스트에 저장
b = daeching.append(list(map(int, input().split())))


cha = []
# A의 원소 중 B의 원소와 중복되지 않은 값을 차 리스트에 저장
for aa in daeching[0] :
  if aa not in daeching[1] :
    cha.append(aa)

# B의 원소 중 A의 원소와 중복되지 않은 값을 차 리스트에 저장
for bb in daeching[1] :
  if bb not in daeching[0] :
    cha.append(bb)

# A와 B의 대칭 차집합의 개수를 출력
print(len(cha))


# set() 함수끼리 연산으로 중복값을 제거할 수 있다.
# a와 b의 리스트의 길이를 빼서 대칭 차집합 구하기
A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a^b))
