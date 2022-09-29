for _ in range(int(input())):
    s = int(input()) # 자동차의 가격 s
    for _ in range(int(input())): # for 반복문 통해 s 순회
        q, p = map(int, input().split()) # 특정 옵션의 개수 q와 해당 옵션의 가격 p int로 형변환
        s += q*p # s에 qxp의 값을 증가시킴
    print(s)