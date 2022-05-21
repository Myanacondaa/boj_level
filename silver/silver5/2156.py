n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

result = [0]*n

result[0] = wine[0] # 첫번째 포도주

if n > 1:    # 두번째 포도주
    result[1] = wine[0]+wine[1]

if n > 2:
    # 포도주가 3잔 이상일 경우
    # 현재 포도주를 선택하는 방법은 총 세가지
    # 1) 전포도주 + 현재 포도주 : wine [i-1] + wine[i]
    # 2) 전전 포도주 + 현재 포도주 : wine[i-2]+wine[i]
    # 3) 현재 포도주 선택 안 함 : result[i-1]
    # 세가지 경우 중 최댓값 선택
    result[2] = max(wine[0]+wine[2], wine[1]+wine[2], result[1])

if n > 3:
    for i in range(3, n):   # (전전전(결과값)+전+현재),(전전+현재),(현재X)
        result[i] = max(result[i-3]+wine[i-1]+wine[i], result[i-2]+wine[i], result[i-1])

print(result[n-1])