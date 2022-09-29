# a,b=map(int,input().split())
# data=[0]
# sum=0

# for i in range(1,b+1):
#   for j in range(i):
#     data.append(i)

# for i in range(a, b+1):
#   sum+=data[i]
# print(sum)

num_list = list(map(int, input().split()))

if len(set(num_list)) == 1:
  print(num_list[0]*1000+10000)
elif len(set(num_list)) == 2:
  if num_list[0] == num_list[1]:
    print(num_list[0]*100+1000)
  elif num_list[0] == num_list[2]:
    print(num_list[1]*100+1000)
  elif num_list[1] == num_list[2]:
    print(num_list[2]*100+1000)
elif len(set(num_list)) == 3:
  print(max(num_list)*100)
