# 당신은 SASA 연못에서 알파벳 S 모양의 블록 $N$개와 알파벳 A 모양의 블록 $M$개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.

# SASA 모형 $1$개를 만들기 위해서는, 알파벳 S 모양의 블록 $2$개와 알파벳 A 모양의 블록 $2$개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.



# S,A = map(int,input().split())

# bc= 0

# while S >= 1 or  A >= 1:
#     if S >= 2 and A >= 2:
#         S -=2
#         A -=2 
#         bc+=1
#     else :
#         print(bc)
#         break

# 제한값이 10의 9승이라 시간제한걸림 반복문말고 나눗셈이나 
S,A = map(int,input().split())

sb= S//2
ab= A//2 

if ab > sb :
    i = ab-sb
    print(ab-i)
elif ab < sb :
    i = sb-ab
    print(sb-i)
elif ab == sb :
    print (ab)