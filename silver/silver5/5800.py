k = int(input())
for i in range(k):
    n = list(map(int, input().split()))
    n.pop(0)        # 반번호 제거
    n.sort()
    gap = -1
    for j in range(1, len(n)):
        if n[j] - n[j-1] > gap:
            gap = n[j] - n[j-1]
    print(f"Class {i+1}")       # 반 번호 출력
    print(f"Max {max(n)}, Min {min(n)}, Largest gap {gap}")


