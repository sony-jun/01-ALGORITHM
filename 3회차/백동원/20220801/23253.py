# 자료구조는 정말 최고야

N, M = map(int,input().split())                 # 이 문제의 가장 핵심은 
possibility = bool                              # 2개 이상의 데이터를 가지고 있는 리스트에서
                                                # 가장 맨 오른쪽 2개의 값을 비교했을 때
for _ in range(M):                              # 2번째 데이터가 첫번째 데이터보다 작으면,
    k = int(input())                            # No를 출력하는 것이다.
    num_list = list(map(int, input().split()))  
    while len(num_list) > 1:                    # 입력값의 길이가 1이 되면 멈추는 반복문 작성
        a = num_list.pop()                      
        b = num_list.pop()                      # 끝에서 두개의 데이터를 뽑음
        if  a > b:                              # 비교하였을때, 첫번째 데이터가 더 크면,
            possibility = False                 # False 값을 저장
            break                               # 이 경우가 발생하면 나머지가 기준에 부합해도 
        else:                                   # No를 출력해야 하기 때문에 반복문 강제종료
            num_list.append(b)                  # pop()은 뺀 결과를 적용하기 때문에 
if possibility == False:                        # 계속 비교하기 위해서는 2번째 값을 다시 추가한다.
    print('No')
else:
    print('Yes')