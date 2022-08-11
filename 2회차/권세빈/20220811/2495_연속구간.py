import sys
sys.stdin = open('2495.txt', 'r')

# 세개의 숫자
for _ in range(3):
    n = list(input())
    cnt = 0
    # 카운트값들을 담을 결과 리스트
    result = [0]

    for i in range(7):

        # n에서 연속하는 숫자가 있다면
        if n[i] == n[i+1]:
            # 카운트 추가
            cnt += 1
            # 결과 리스트에 추가
            result.append(cnt)
        # 아니라면 카운트 초기화
        else:
            cnt = 0
    # 결과 리스트중 가장 큰값을 꺼내고
    # 개수 셀 때 하나씩 제외되었던 연속 숫자를 추가해줌
    print(max(result)+1)