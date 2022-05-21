n = int(input())        # 후보자 수, 다솜이는 0번
candidate = [0]*n
for i in range(n):
    candidate[i] = int(input())

cnt = 0     # 돈으로 매수해야 하는 사람 수
while max(candidate) != candidate[0]:   # 기호 0번이 최댓값이 될때까지 반복
    # 최댓값을 가진 인덱스에 해당하는 값에서 1 빼고, 기호 0번에 1 추가
    candidate[candidate.index(max(candidate))] -= 1
    candidate[0] += 1
    cnt += 1

if candidate[0] in candidate[1:]:     # 다정이와 득표가 같은 후보자가 있는 경우
    cnt += 1

print(cnt)