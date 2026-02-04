# 직각삼각형 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120823
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 02. 04. 17:59:47

n = int(input())
for i in range(n+1):
    if i == 0:
        continue
    print('*' * i)