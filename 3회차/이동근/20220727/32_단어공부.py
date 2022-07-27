S = list(input().lower())
# https://velog.io/@yeonu/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EA%B0%81%EC%A2%85-%EB%A9%94%EC%84%9C%EB%93%9C
D = dict.fromkeys(S, 0)
for i in S:
    D[i] += 1
    
dupli = list(D.values())
# https://wikidocs.net/16039
if dupli.count(max(dupli)) > 1:
    print("?")
else:
    # https://velog.io/@haileeyu21/TIL-Dictionary-%EB%82%B4%EB%B6%80%EC%97%90%EC%84%9C-value%EA%B0%80-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EA%B2%83-%EC%B0%BE%EA%B8%B0
    print(max(D, key=D.get).upper())