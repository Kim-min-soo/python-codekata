# 입양 시각 구하기(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59413
# 작성자: 김민수
# 작성일: 2026. 01. 16. 14:37:11

-- 코드를 입력하세요
SELECT 
    h.hour as HOUR,
    COALESCE(a.cnt, 0) as COUNT
FROM
(select 0 as hour UNION ALL select 1 UNION ALL select 2 UNION ALL select 3 UNION ALL select 4 UNION ALL select 5 UNION ALL select 6 UNION ALL select 7 UNION ALL select 8 UNION ALL select 9 UNION ALL select 10 UNION ALL select 11 UNION ALL select 12 UNION ALL select 13 UNION ALL select 14 UNION ALL select 15 UNION ALL select 16 UNION ALL select 17 UNION ALL select 18 UNION ALL select 19 UNION ALL select 20 UNION ALL select 21 UNION ALL select 22 UNION ALL select 23) h
LEFT JOIN(
SELECT
    HOUR(DATETIME) as hour,
    COUNT(*) AS cnt
FROM
    ANIMAL_OUTS
GROUP BY
    HOUR(DATETIME)
) a
ON h.hour = a.hour
ORDER BY h.hour