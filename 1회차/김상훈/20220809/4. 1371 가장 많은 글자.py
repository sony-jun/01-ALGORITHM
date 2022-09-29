from collections import Counter
import sys
sys.stdin = open("4. 가장 많은 글자.txt", "r")


s = sys.stdin.read()
s=s.replace(' ','')
s=s.replace('\n','')
print(s)
result = []

count = Counter(s).most_common()

for i in range (len(count)): 
    if(count[0][1]==count[i][1]):
        result.append(count[i][0])
        
    else:
        break
result.sort()
print(''.join(result))

    
    