-- 코드를 입력하세요
# 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 조회
# JULY에 FLAVOR가 같은 것이 여러 개 있다.
SELECT FLAVOR
FROM(
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDERS
    FROM (
        SELECT FLAVOR, TOTAL_ORDER FROM JULY
        UNION ALL
        SELECT FLAVOR, TOTAL_ORDER FROM FIRST_HALF
    ) combined_table
    GROUP BY FLAVOR
    ORDER BY TOTAL_ORDERS DESC
) as top_tables
LIMIT 3;