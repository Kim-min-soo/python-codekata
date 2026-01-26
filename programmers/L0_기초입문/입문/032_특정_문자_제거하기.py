# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 26. 09:10:40

def solution(my_string, letter):
    new_my_string = ""
    for i in my_string:
        if i == letter :
            continue
        new_my_string+=i
    return new_my_string