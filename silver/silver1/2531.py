import sys
input = sys.stdin.readline
# 초밥 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())
susi = [int(input()) for _ in range(n)]
lp, rp, res = 0, k, 0    # 왼쪽 포인터, 오른쪽 포인터, 결과값
tmp = set()
while lp < n:   # 왼쪽 포인터가 리스트 끝까지 오면 반복 종료
    if lp < rp:     # 왼쪽 포인터가 오른쪽 포인터보다 작으면
        tmp = set(susi[lp:rp])      # 중복된 번호를 제외하기 위해 집합 사용

    elif lp > rp:       # 왼쪽 포인터가 더 크면 오른쪽 포인터는 한 바퀴를 돌게 된 것임
        tmp = set(susi[lp:]) | set(susi[:rp+1])  # 왼쪽 포인터와 오른쪽 포인터 따로 계산 후 합침

    # 집합 안에 쿠폰 번호가 있으면 쿠폰 사용 필요 없고
    # 쿠폰 번호 없으면 새로운 쿠폰 번호의 초밥 먹을 수 있으므로 +1 추가
    res = max(res, len(tmp)) if c in tmp else max(res, len(tmp) + 1)

    lp, rp = lp+1, rp+1
    if rp == n+1:       # 오른쪽 포인터가 끝까지 왔다면
        rp = 0      # 맨 앞으로

print(res)