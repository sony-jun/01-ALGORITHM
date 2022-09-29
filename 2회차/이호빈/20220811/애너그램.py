t = int(input())
result = []
for _ in range(t):
    gram, gram1 = map(str, input().split())
    
    s_gram = sorted(list(gram))
    s_gram1 = sorted(list(gram1))  


    if s_gram == s_gram1:
        print(f"{gram} & {gram1} are anagrams.")
    else:
        print(f"{gram} & {gram1} are NOT anagrams.")

    