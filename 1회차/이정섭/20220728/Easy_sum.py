a,b=map(int,input().split())
data=[0]
sum=0

for i in range(1,b+1):
  for j in range(i):
    data.append(i)

for i in range(a, b+1):
  sum+=data[i]
print(sum)

# Alt 1

# a,b = map(int,input().split())
 
# arr = [0]
# for i in range(46):
#     for j in range(i):
#         arr.append(i)
 
# print(sum(arr[a:b+1]))

# a, b의 범위는 1,000까지였기 때문에 반복문의 범위는 46까지만 구해도 된다. (len(arr) = 1036)
# i값을 기준으로 이중 반복문을 사용하는데 빈 arr에 i를 추가한다. 
# 값이 1부터 arr에 들어간다. (j를 추가하는 것이 아님!!)
# sum함수를 이용해서 풀었다.(구간합을 구하지 않고 기존 arr에서 사용 가능하다.)
# 구간 합을 구할 때 누적 합을 구하지 않고도 sum + slicing 함수로 구할 수 있다는 것을 배웠다.