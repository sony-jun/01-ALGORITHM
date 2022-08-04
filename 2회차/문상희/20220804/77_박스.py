test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())

    seet = []

    for i in range(n):
        line = list(map(int, input().split()))
        seet.append(line)
        # n행만큼 m자리 문자열을 입력받아 리스트로 변환한 값을 빈 리스트에 넣어줍니다.
    cnt = 0

    for j in range(m):
        stripe = []
        for i in range(n):
            stripe.append(seet[i][j])
        stripe = stripe[::-1]
        # seet형태에서 아래가 0이면 1들이 한 칸씩 내려오는 구조이므로 맨 뒷값부터 앞으로 오면서
        # 확인을 해 주어야 하지만 정방향이 보기 편하여 뒤집어 주었습니다.
        for i in range(n):
            if stripe[i] == 0:
                cnt += stripe[i:].count(1)
        # 0이 나온 자리에서 그 이후에 1이 있으면 모든 1이 0 자리로 1칸씩 움직일것이므로
        # 문자열의 그 자리부터 1이 몇개인지 세어 cnt에 값을 추가하여줍니다.
    print(cnt)