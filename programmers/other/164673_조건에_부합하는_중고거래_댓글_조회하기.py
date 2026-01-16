# 조건에 부합하는 중고거래 댓글 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164673
# 작성자: 김민수
# 작성일: 2026. 01. 16. 09:39:49

-- 코드를 입력하세요
SELECT
    B.TITLE,
    B.BOARD_ID,
    R.REPLY_ID,
    R.WRITER_ID,
    R.CONTENTS,
    DATE_FORMAT(R.CREATED_DATE,'%Y-%m-%d') AS CREATED_DATE
FROM
    USED_GOODS_BOARD B INNER JOIN USED_GOODS_REPLY R
    ON B.BOARD_ID = R.BOARD_ID
WHERE 
    B.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY
    CREATED_DATE,
    B.TITLE