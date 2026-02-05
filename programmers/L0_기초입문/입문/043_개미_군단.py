# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 02. 05. 09:18:02

def solution(hp):
    jang_ant = hp//5
    resume1 = hp % 5
    byung_ant = resume1//3
    ill_ant = resume1 % 3
    ant = jang_ant + byung_ant + ill_ant
    return ant