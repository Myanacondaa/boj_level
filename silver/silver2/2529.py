from itertools import permutations
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
inequality = list(map(str, input().split()))
res = []
for per in permutations(num, n+1):
    check = True
    for i in range(n):
        if inequality[i] == '>':
            if per[i] < per[i+1]:
                check = False
                break

        else:
            if per[i] > per[i+1]:
                check = False
                break

    if check:
        res.append(per)

print(''.join(map(str, max(res))))
print(''.join(map(str, min(res))))
