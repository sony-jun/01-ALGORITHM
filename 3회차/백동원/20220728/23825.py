# SASA 모형을 만들어보자

S, A = map(int, input().split())    
if S // 2 >= A // 2:            # 입력 받은 두 수를 2로 나눠 몫을 구한다.
    print(A // 2)               # 그 중 작은 몫이 있으면 출력하고
else:                           # 같으면 아무 몫이나 출력
    print(S // 2)