arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)  #입력받은 값을 42로 나눈 나머지를 arr에 저장 n = [39, 40, 41, 0, 1, 2, 40, 41, 0, 1]
arr = set(arr) #set으로 중복 제거 [0, 1, 2, 39, 40, 41]
print(len(arr))