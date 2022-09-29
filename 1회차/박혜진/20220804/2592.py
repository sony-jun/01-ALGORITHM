# 런타임에러 -> 정답코드
# 10개의 자연수를 입력받아 평균과 최빈수 구하기

nums = []
for _ in range(10) :
  nums.append(int(input()))

max_nums = []
for i in nums :
  # 몇 번 입력받았는지 숫자를 세기
  max_nums.append(nums.count(i))

print(sum(nums)//len(nums))
# 가장 많이 입력받은 횟수의 인덱스 값이 그 숫자값 
print(nums[max_nums.index(max(max_nums))])

# 정답 코드
numbers = [int(input()) for i in range(10)]

print(sum(numbers)//10)

# max함수의 key 파라미터를 사용한 방법
# 람다를 이용해서 풀 수도 있음
print(max(numbers, key = numbers.count))