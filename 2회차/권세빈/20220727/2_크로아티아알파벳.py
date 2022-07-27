# https://www.acmicpc.net/problem/2941


word = input()
l = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in l:
    word = word.replace(i,'a')
print(len(word))

# word = input()
# l = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# result = 0
# for i in l:
#     result += word.count(i)
# print(len(word) - result)






