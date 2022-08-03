A, B = map(str, input().split())

answer_min = int(A.replace('6','5')) + int(B.replace('6', '5'))
answer_max = int(A.replace('5','6')) + int(B.replace('5', '6'))


print(answer_min, answer_max)