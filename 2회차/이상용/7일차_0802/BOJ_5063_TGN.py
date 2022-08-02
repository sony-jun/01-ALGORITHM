# 이건 문제가 왜 이러냐
test_case = int(input())
for i in range(test_case):
  r, e, c = map(int, input().split())
  if r > e - c:
    print('do not advertise')
  elif r == e - c: 
    print('does not matter')
  else:
    print('advertise')

# r : 광고를 하지 않았을 때 수익
# e : 광고를 했을 때의 수익
# c : 광고 비용