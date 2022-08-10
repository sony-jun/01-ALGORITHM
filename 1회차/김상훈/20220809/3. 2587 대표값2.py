import sys
sys.stdin = open("3. 대표값2.txt", "r")

input = sys.stdin.readline

T = 5
numbers_list = []
for _ in range(T):
    n = int(input()) # 테스트 케이스만큼 수 입력
    numbers_list.append(n) # 수 리스트에 저장
    
avg = sum(numbers_list) // T # 평균 = 리스트 내 숫자 합에서 숫자 갯수만큼 나눔

print(avg)
numbers_list.sort() # 오름차순 정렬
print(numbers_list[T//2]) # 리스트의 [숫자 갯수//2] 요소를 출력