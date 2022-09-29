# 주어진 테스트 케이스를 받음 
tc = int(input())

# 테스트 케이스의 range 처음부터 끝까지 돌음
for _ in range(tc) :
    # map함수 통해서 쪼개고 int로 형변환
    r, e, c = map(int, input().split())
    # (광고를 했을 때 수익 - 광고 비용)이 광고를 하지 않았을 때 수익보다 크면
    if e - c > r :
        # 광고 해야함 출력
        print("advertise")
    # 같으면 
    elif e - c == r :
        # 수익 차이 없음 출력
        print("does not matter")
    # 광고를 하지 않았을 때 수익보다 작으면
    else :
        # 하지 않아야함 출력
        print("do not advertise")