# 입력받을 문장의 개수
for _ in range(int(input())) :

    # 문장을 입력받아 리스트로 만들기
    a = list(input().split())

    new_a = []
    # 입력받은 문장의 단어를 하나씩 꺼내어 거꾸로 뒤집기
    for i in a :
        i = i[::-1]
        new_a.append(i)

    for aa in new_a :
      print(aa, end=' ')