def self_num(num) :

  for i in list(str(num)) :
    num += int(i)

  return num

num_list = []

for i in range(10000) :
  num_list.append(self_num(i))

for o in range(10000) :
  if o in num_list :
    pass

  else :
    print(o)
  
