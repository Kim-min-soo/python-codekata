# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 22. 09:05:45

def solution(str1, str2):
    if str1.find(str2) == -1:
        return 2
    else :
        return 1