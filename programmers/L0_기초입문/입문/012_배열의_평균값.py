# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 19. 08:59:33

def solution(numbers):
    sum_n = 0
    for i in numbers :
        sum_n += i
    return sum_n/len(numbers)