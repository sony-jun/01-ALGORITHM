# 입력받은 수만큼 테스트 케이스 반복
for i in range(int(input())) :

  # r : 광고를 하지 않을 때 수익
  # e : 광고를 했을 때 수익
  # c : 광고 비용
  r, e, c = map(int, input().split())

  # 광고를 하지 않았을 때의 수익이 광고 비용을 제외한 광고를 했을 때의 수익보다 크면 광고를 하지 않고
  # 반대의 경우 광고를 한다. 단, 두 비용의 차이가 없으면 상관없음을 출력

  if r < e - c :
    print('advertise')

  elif r == e - c :
    print('does not matter')
  
  else :
    print('do not advertise')