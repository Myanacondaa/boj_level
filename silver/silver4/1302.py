from collections import Counter

n = int(input())
book = []
for _ in range(n):
    book.append(input())

# 개수의 내림차순, 책 제목의 오름차순으로 정렬
result = sorted(Counter(book).items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])