# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 01. 27. 09:04:25

def solution(n):
    num = 0
    while(1):
        if n<=0 :
            break    
        k = n % 10
        num += k
        n = n//10
    return num