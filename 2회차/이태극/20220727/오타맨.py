# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON

for i in range(int(input())):
    idx,word=input().split()
    idx=int(idx)-1
    word=list(word)
    word.pop(idx)
    print("".join(word))