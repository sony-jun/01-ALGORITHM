# 유니크

N = int(input())
score = []
list_ = []
result = [0] * N                            # 출력용 리스트

for _ in range(N):                          # 2차원 배열 생성
    line = list(map(int, input().split()))
    score.append(line)

for _ in range(3):

    for a in score:                         
        list_.append(a[_])                  # 같은 인덱스로 이루어진 임시리스트 생성 (열 리스트)

    for b in range(N):                      
        if list_.count(list_[b]) == 1:      # 만약 열 내에 같은 번호가 없다면,
            result[b] += list_[b]           # 결과리스트의 인덱스에 값 더함
    list_ = []                              # 열 리스트 초기화

for d in result:
    print(d)