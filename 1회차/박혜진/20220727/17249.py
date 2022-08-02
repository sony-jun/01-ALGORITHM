face = input()

left_cnt = 0
right_cnt = 0

for i in face :
  if i == '@' :
    left_cnt += 1  
  if i == '0' :
    break

for i in face[::-1] :
  if i == '@' :
    right_cnt += 1
  if i == '0' :
    break

print(left_cnt, right_cnt)