# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 21. 09:05:38

def solution(sides):
    sort_sides = sorted(sides)
    if sort_sides[2] < sort_sides[0]+sort_sides[1]:
        return 1
    else:
        return 2