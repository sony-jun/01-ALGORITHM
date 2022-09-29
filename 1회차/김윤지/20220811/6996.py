


n = int(input())

for _ in range(n):
    a , b = map(str, input().split())

    sa = sorted(list(a)) #리스트로변환 후 정렬
    sb = sorted(list(b))

    if sa == sb: #두 단어의 요소가 같으면
        print(a +"&"+ b + "are anagrams.")
    else:
        print(a +"&"+ b + "are NOT anagrams.")