def solution(n, k):
    suv = n // 10 #서비스 음료수의 수
    print(suv)
    answer = 12000 * n + 2000 * (k - suv)
    return answer