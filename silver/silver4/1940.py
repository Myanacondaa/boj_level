n = int(input())
m = int(input())
material = list(map(int, input().split()))
material.sort()
res = 0
pl = 0  # 맨 앞 인덱스
pc = n-1     # 맨 끝 인덱스
while pl < pc:
    sum_material = material[pl] + material[pc]
    if sum_material == m:
        res += 1
        pl += 1
        pc -= 1

    elif sum_material < m:
        pl += 1

    else:
        pc -= 1

print(res)