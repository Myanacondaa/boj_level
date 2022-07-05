# 유사 회문 판단
def pseudo(arr: list[str], left: int, right: int) -> bool:
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# 회문 판단
def palindrome(x: list[str], left: int, right: int) -> int:
    while left < right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            res1 = pseudo(x, left+1, right)
            res2 = pseudo(x, left, right-1)
            if res1 == True or res2 == True:
                return 1
            else:
                return 2
    return 0


t = int(input())
for i in range(t):
    s = list(input())
    print(palindrome(s, 0, len(s)-1))
