# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 17. 22:43:29

def solution(n, k):
    # n이 10일때마다 k는 +1
    service_k = n // 10
    return n*12000 + (k-service_k)*2000