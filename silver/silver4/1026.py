n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)        # a는 역정렬
b.sort()                    # b는 정렬
sum_arr = 0
for i in range(n):
    sum_arr += a[i]*b[i]        # a*b는 작은수 * 큰수이므로 최종 합은 최솟값이 됨

print(sum_arr)