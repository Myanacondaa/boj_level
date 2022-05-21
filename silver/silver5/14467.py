dic = {}
for i in range(10):
    dic[i+1] = -1
n = int(input())        # 관찰 횟수
cnt = 0
for i in range(n):
    cow, location = map(int, input().split())
    if dic[cow] != -1:        # 해당 번호의 소의 키값이 비어있지 않고
        if dic[cow] != location:    # 그 소의 위치가 다를 경우
            cnt += 1        # 소가 다리를 건넌 경우이기 때문에 cnt 1 증가
    dic[cow] = location

print(cnt)
