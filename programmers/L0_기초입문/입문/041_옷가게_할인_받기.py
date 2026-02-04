# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 02. 04. 11:55:22

import math
def solution(price):
    if price >= 500000:
        return math.floor(price * (1-0.2))
    if price >= 300000:
        return math.floor(price * (1-0.1))
    if price >= 100000:
        return math.floor(price * (1-0.05))
    return price