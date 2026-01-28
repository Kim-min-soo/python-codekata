# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 28. 09:02:35

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer