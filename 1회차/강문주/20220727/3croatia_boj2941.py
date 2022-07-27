croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # 크로아티아 i변수에 있는것을 *로 대체
print(len(word))
'''
몇개의 크로아티아어로 이뤄져있나'''