text = input()

# 대문자로 바꿔서 저장
value = text.upper()
# set() 함수로 중복된 값 제거하고 문자열 집합을 담음
values = list(set(value))

maxcount = 0

# for문으로 values(M,I,S,P)가
for i in range(len(values)):
    # value에 몇 개 있는지 확인
    cnt = value.count(values[i])
    # 값이 최대값이면
    if cnt == maxcount:
        # maxcount에 저장
        maxcount = cnt
        # 최대값이 여러 개 존재하면 ? 출력 조건 
        maxchar = '?' 
        
        # 예시) values(M,I,S,P)의 values[i] = values[0] = M
        # value.count(values[i]) = M의 개수 1, 그래서 cnt = 1

    elif cnt > maxcount:
        # values[0] = M 이면 cnt = 1
        maxcount = cnt # 1
        maxchar = values[i] # M
    else:
        pass

print(maxchar.upper())