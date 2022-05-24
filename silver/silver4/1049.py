n, m = map(int, input().split())
brand = []
for _ in range(m):
    brand.append(list(map(int, input().split())))

set_line = sorted([x[0] for x in brand])[0]     # 6개 묶음 상품 중 가장 싼 가격
single = sorted([x[1] for x in brand])[0]     # 단일 상품 중 가장 싼 가격

price = 0

if set_line <= single*6:        # 6개 묶음 상품이 단일 상품 *6보다 저렴하면
    # 6개 묶음 상품과 단일 상품 각각 구매하여 정확하게 n개를 맞춤
    price = set_line*(n//6) + single*(n % 6)
    if set_line < single*(n % 6):     # n개를 넘어도 세트 상품을 사는 것이 저렴하면
        price = set_line*(n//6+1)  # 세트 상품만 구매
    print(price)

else:
    print(single*n)