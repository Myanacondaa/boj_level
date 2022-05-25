from itertools import permutations
n = int(input())        # 카드의 개수
k = int(input())        # 뽑는 카드의 수
a = []
for _ in range(n):
    a.append(input())

res = set()     # 숫자 조합의 결과가 중복될 수 있으므로 집합으로 결과를 냄
for per in permutations(a, k):    # 순열 리스트
    res.add(''.join(per))        # 두 숫자를 조합 후 삽입

print(len(res))
