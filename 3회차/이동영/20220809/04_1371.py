import sys

sys.stdin = open("input.txt", "r")

dict_ = dict()
str_ = ''
max_list =[]

while True:
    try :
        temp = input()
        str_ += temp
    except(EOFError):
        break

str_ = str_.replace(' ','')

for i in str_:

    if i in dict_:
        dict_[i] += 1

    else:
        dict_[i] = 1

max_ = max(dict_, key=dict_.get)

for i in dict_.keys():
    if dict_[i] == dict_[max_]:
        max_list.append(i)

max_list.sort()

print(''.join(max_list))