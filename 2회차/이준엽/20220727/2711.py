# t = int(input())

# for i in range(t):
#     ota_number, word = input().split()
#     word = list(word)
#     del(word[int(ota_number)-1])
#     word = ''.join(word)
#     print(word)

t = int(input())

for i in range(t):
    otanum, word = input().split()
    f_num = int(otanum)-1
    word = word[:(int(otanum)-1)]+word[int(otanum):]
    print(word)
# word = 'apple'
# print(word[0:0])