N = input()
num = N
cnt = 0

while 1:
  if len(num) == 1:
    num = "0" + num
  plus = str(int(num[0]) + int(num[1]))
  num = num[-1] + plus[-1]
  cnt += 1
  if num == N:
    print(cnt)
    break