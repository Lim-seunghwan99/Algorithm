-- 코드를 입력하세요
SELECT FLOOR(PRICE/10000) * 10000 AS PRICE_GROUP, COUNT(*) PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;