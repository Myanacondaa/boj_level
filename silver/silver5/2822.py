score = []
for i in range(8):
    score.append(int(input()))

final_score = sorted(score, reverse=True)[:5]
idx = []
for i in range(5):
    idx.append(score.index(final_score[i])+1)

print(sum(final_score))
for i in sorted(idx):
    print(i, end=' ')

