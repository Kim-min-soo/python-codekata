# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 김민수
# 작성일: 2026. 02. 27. 09:43:17

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// box_len은 배열 box의 길이입니다.
int solution(int box[], size_t box_len, int n) {
    int width, length, height = 0;
    width = box[0]/n;
    length = box[1]/n;
    height = box[2]/n;
    int answer = width * length * height;
    return answer;
}