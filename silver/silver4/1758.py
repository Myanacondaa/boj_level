n = int(input())
tip = []
for _ in range(n):
    tip.append(int(input()))

# 정렬을 한 뒤 큰수에서 0부터 1씩 빼기
tip.sort(reverse=True)

for i in range(n):
    tip[i] -= i
    if tip[i] <= 0:     # 0이 나오는 순간 그 뒤에는 무조건 0보다 작거나 같으므로 계산 필요 X
        tip[i:] = [0]
        break

print(sum(tip))