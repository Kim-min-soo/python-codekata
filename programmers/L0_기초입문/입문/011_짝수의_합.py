# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 19. 08:57:31

def solution(n):
    even_sum = 0
    for i in range(n+1):
        if i % 2 == 0 :
            even_sum += i
    return even_sum