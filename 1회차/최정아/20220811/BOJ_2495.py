for _ in range(3):
    s = input()
    len_max = 0 # 가장 긴 길이 
    cnt = 1 # 같은 숫자가 나오면 넣음
    for i in range(1, len(s)):
        if s[i-1] == s[i]: # 이전 숫자와 같으면 1씩 증가
            cnt += 1
        else: # 아니면 1
            cnt = 1

        if cnt > len_max: # cnt가 더 큰 숫자이면 max를 cnt로
            len_max = cnt
    print(len_max)