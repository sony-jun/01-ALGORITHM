x, y = map(str, input().split())
        # 숫자를 string 변환. 거꾸로 하기 위해.

rev_x = int(x[::-1])
rev_y = int(y[::-1])
        # 거꾸로하고 다시 정수로 변환. 더하기 위해.
        
rev_s = str(rev_x + rev_y)
        # 더하고 문자로 변화. 거꾸로하기 위해.

print(int(rev_s[::-1]))