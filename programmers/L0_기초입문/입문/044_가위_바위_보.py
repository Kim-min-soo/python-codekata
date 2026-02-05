# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 02. 05. 09:40:49

def solution(rsp):
    win_str = ""
    for i in rsp:
        if i == '2' :
            win_str += '0'
        elif i == '0':
            win_str += '5'
        elif i == '5':
            win_str += '2'
    return win_str