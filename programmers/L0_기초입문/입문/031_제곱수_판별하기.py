# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 26. 08:58:57

def solution(n):
    for i in range(n):
        if i**2 == n:
            return 1
    return 2