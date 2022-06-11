import sys
sys.setrecursionlimit(10**5)


def hanoi(n, peg1, peg2, peg3):
    if n == 1:
        print(f'{peg1} {peg3}')
        return
    else:
        hanoi(n-1, peg1, peg3, peg2)
        hanoi(1, peg1, peg2, peg3)
        hanoi(n-1, peg3, peg1, peg2)


# 원반이 n개인 하노이 타워의 이동 횟수 k = 2**n - 1

n = int(input())
print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)