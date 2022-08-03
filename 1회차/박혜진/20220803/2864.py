a, b = input().split()

# 입력받은 문자열에 5가 있으면 6으로 변경하여 최대값을 만들기
big = int(a.replace('5', '6')) + int(b.replace('5', '6'))

# 입력받은 문자열에 6이 있으면 5로 변경하여 최소값을 만들기
mini = int(a.replace('6', '5')) + int(b.replace('6', '5'))

print(mini, big)
