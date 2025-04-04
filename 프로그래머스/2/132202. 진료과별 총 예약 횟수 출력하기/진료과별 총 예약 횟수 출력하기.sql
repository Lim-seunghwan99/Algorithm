-- 코드를 입력하세요
# 2022년 5월에 예약한 환자 수를 진료과 코드 별로 조회
SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
FROM APPOINTMENT
WHERE month(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD;