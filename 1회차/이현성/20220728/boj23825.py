S, A = map(int, input().split()) # input값을 각 각 S, A에 int로 할당

mok_ = [] # 빈 몫 list 

mok_.append(S // 2) # S를 2로 나눴을 때 몫을 mok_ list에 저장
mok_.append(A // 2) # A를 2로 나눴을 때 몫을 mok_ list에 저장

print(min(mok_)) # 몫 리스트 중에 가장 작은 값을 출력
