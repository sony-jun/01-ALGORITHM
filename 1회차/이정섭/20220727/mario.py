# t = int(input())         10 inputs onl so no need t
# m = []
# score = 0
# for i in range(t):
#     m.append(int(input()))
# for j in m:
#     score += j
#     if score >= 100:
#         if score - 100 > 100 - (score - j):
#             score -= j
#         break
# print(score)

m_score = []    # made a list for a input
score = 0
for i in range(10):
    m_score.append(int(input()))
for j in m_score:   # index in 'm list' (m_score = [])
    score += j
    if score >= 100:
        if score - 100 > 100 - (score - j):
            score -= j
        break
print(score)

# score can added in order of input
# each score(input) is equal or less than 100
# the sum of output should be around 100
# when the out put is over 100, compare before and after the last score in added
# chose the added score that has less gap between before and after score has added

# if sum > 100
#  break
