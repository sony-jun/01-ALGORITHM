# mush = []
# for i in range(10):
#     mush.append(int(input()))
# #print(mush)

# score = 0
# score_num = []
# score_onem = 0
# for i in mush:
#     score += i
#     if score <= 100:
#         score_num.append(score)
#         score_onem = score
#     else:
#         score_onem = score
#         #print(score_exc)
#         break
# #print(score_num[-1])

# score_small = 100 - score_num[-1]
# score_big = score_onem - 100
# #print(score_small, score_big)
# if score_small >= score_big:
#     print(score_onem)
# else:
#     print(score_num[-1])





mush = []
for i in range(10):
    mush.append(int(input()))
#print(mush)

score = 0
score_num = 0
score_onem = 0
for i in mush:
    score += i
    if score <= 100:
        score_num = score
        score_onem = score
    else:
        score_onem = score
        #print(score_exc)
        break
#print(score_num[-1])

score_small = 100 - score_num
score_big = score_onem - 100
#print(score_small, score_big)
if score_small >= score_big:
    print(score_onem)
else:
    print(score_num)