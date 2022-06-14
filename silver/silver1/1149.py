import sys
input = sys.stdin.readline

def rgb_distance(x:list[list[int]]) ->int: #dp 알고리즘
    for i in range(1, len(x)):
        x[i][0] += min(x[i-1][1], x[i-1][2])
        x[i][1] += min(x[i-1][0], x[i-1][2])
        x[i][2] += min(x[i-1][0], x[i-1][1])
    return min(x[-1][0], x[-1][1], x[-1][2])



if __name__ == "__main__":
    N = int(input())
    house = []
    for _ in range(N):
        house.append(list(map(int, input().split())))

    print(rgb_distance(house))
