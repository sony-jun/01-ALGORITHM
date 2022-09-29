n = int(input())
cnt1 = 0 # 행에서의 갯수
cnt2 = 0 # 열에서의 갯수

a = [list(input()) for _ in range(n)]
# 행에서 찾기
for i in range(n):
    list_ = [] # '.'을 담을 리스트
    for j in range(n):
        if a[i][j] == '.': 
            list_.append('.')
        else: # '.'을 리스트에 담다가 다른게 나오면 리스트의 길이가 2인지 확인하고 카운팅
            if len(list_) >= 2:
                cnt1 += 1
                list_ = [] #다시 리스트를 비우고 '.' 담음
            else:
                list_ = []
    if len(list_) >= 2:
        cnt1 += 1
# 열에서 찾기
for i in range(n):
    list_ = []
    for j in range(n):
        if a[j][i] == '.': 
            list_.append('.')
        else:
            if len(list_) >= 2:    
                cnt2 += 1
                list_ = []
            else:
                list_ = []
    if len(list_) >= 2 :
        cnt2 += 1

print(cnt1, cnt2)