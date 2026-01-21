# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 22. 08:56:46

def solution(n, numlist):
    del_numlist = []
    for i in numlist:
        if i % n == 0:
            del_numlist.append(i)
    return del_numlist