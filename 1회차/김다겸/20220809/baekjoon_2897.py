r, c = map(int, input().split())

# 입력받아서 리스트로 저장
park = [list(input()) for _ in range(r)]
# 답 넣을 리스트 생성
ans = [0] * 5

# 주차장 순회
for i in range(r-1):
    for j in range(c-1):
        # 네개의 주차공간 저장할 리스트 생성
        lot = []
        # 네개의 주차공간 저장
        lot.append(park[i][j])
        lot.append(park[i][j+1])
        lot.append(park[i+1][j])
        lot.append(park[i+1][j+1])
        # 문제 조건에 맞게 답 도출
        if lot.count('.') == 4:
            ans[0] += 1
        elif lot.count('.') == 3 and lot.count('X') == 1 :
            ans[1] += 1
        elif lot.count('.') == 2 and lot.count('X') == 2 :
            ans[2] += 1
        elif lot.count('.') == 1 and lot.count('X') == 3 :
            ans[3] += 1
        elif lot.count('.') == 0 and lot.count('X') == 4 :
            ans[4] += 1
for i in ans:
    print(i)