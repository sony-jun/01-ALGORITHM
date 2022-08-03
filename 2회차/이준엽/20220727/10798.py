word_list = []
for i in range(5):
    word = input()
    word_list.append(word)
new_words = ['' for i in range(15)]
for i in word_list:
    for j in range(15):
        if j >= len(i):
            pass
        else:
            new_words[j]+=i[j]
for i in new_words:
    print(i,end='')