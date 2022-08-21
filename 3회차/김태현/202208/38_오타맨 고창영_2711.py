N = int(input())

for i in range(N):
    num, word = input().split()
    num = int(num)
    word_list = list(word)
    del word_list[num - 1]
    print("".join(word_list))