n, m = map(int, input().split())
card = sorted(list(map(int, input().split())))

for _ in range(m):
    tmp = card[0]+card[1]
    card[0] = tmp
    card[1] = tmp

    card.sort()

print(sum(card))