import sys

# 두 수를 입력받는다.
a, b = map(str, sys.stdin.readline().split())

# 입력받은 두 수를 역순으로 더한다.
n = str(int(a[::-1]) + int(b[::-1]))

# 더한 두 수를 역순으로 변환해 출력
print(int(n[::-1]))