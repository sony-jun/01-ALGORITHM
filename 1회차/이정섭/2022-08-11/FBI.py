data = []

for _ in range(5) :
  data.append(input())

cnt = 0
for i in range(len(data)) :
  if 'FBI' in data[i] :
    print(i+1, end=' ')
    cnt = 1

if cnt == 0 :
  print('HE GOT AWAY!')