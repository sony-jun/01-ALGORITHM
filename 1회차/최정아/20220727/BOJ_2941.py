s=input()
num=0
list=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in list:
  if i in s:
    s=s.replace(i, '_')
print(len(s))