# 1292
""" 
1. 범위의 끝을 나타내는 수는 1,000을 넘을 수 없으므로 길이가 1000에 가깝게 수열을 생성한다.
2. 수열은 해당하는 숫자를 그 수만큼 나열하는 식으로 전개된다.
3. 주어진 구간의 시작과 끝을 슬라이싱하여
4. 그 합을 구한다.
5. 근데 틀렸다. 이유가 뭘까?

"""

# 구간을 저장할 리스트
hap = []
# 수열을 저장할 리스트
numbers = ''
A ,B  = map(int, input().split())
for num in range(1, B):
    numbers += str(num) * num
# print(numbers)

print(sum(map(int, numbers[A - 1:B])))
print(numbers[A - 1:B])
print(numbers, len(numbers), sep = '\n')