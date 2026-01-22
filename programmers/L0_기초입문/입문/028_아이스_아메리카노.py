# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 22. 09:02:00

def solution(money):
    americano = money // 5500
    re_money = money % 5500
    result = [americano, re_money]
    return result