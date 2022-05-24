n = int(input())
card = set(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
for i in num:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
