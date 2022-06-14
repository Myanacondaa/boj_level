import sys
sys.setrecursionlimit(10**5)
n, r, c = map(int, input().split())

result = 0


def search_z(x: int, y: int, size: int):
    global result
    if x == r and y == c:
        print(result)
        exit(0)

    if size == 1:
        result += 1
        return

    if not (x <= r < x+size and y <= c < y+size):   # 내가 찾고자 하는 사분면이 아닐 때
        result += size**2
        return

    tmp = size//2
    search_z(x, y, tmp)             # 2사분면
    search_z(x, y+tmp, tmp)         # 1사분면
    search_z(x+tmp, y, tmp)         # 3사분면
    search_z(x+tmp, y+tmp, tmp)     # 4사분면


search_z(0, 0, 2**n)
print(result)