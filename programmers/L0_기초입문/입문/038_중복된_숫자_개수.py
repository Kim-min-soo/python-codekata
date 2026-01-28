# 중복된 숫자 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 28. 09:15:37

def solution(array, n):
    count = 0
    for i in array:
        if n == i:
            count += 1
    return count