# https://www.acmicpc.net/problem/2941

word = input()
croatia_list = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for char in croatia_list:
    word = word.replace(char, '!')
print(len(word))