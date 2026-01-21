# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 22. 08:58:35

def solution(strlist):
    len_strlist = []
    for i in strlist:
        len_strlist.append(len(i))
    return len_strlist