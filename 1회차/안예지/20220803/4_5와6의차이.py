# 2864.
"""


"""
word = input()
word_min = word.replace('6', '5')
word_max = word.replace('5', '6')
min_ = sum(map(int, word_min.split()))
max_ = sum(map(int, word_max.split()))
print(min_, max_)

