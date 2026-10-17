"""
SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT id, num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_1,
        LAG(num, 2) OVER (ORDER BY id) AS prev_2
    FROM Logs
) ncTable
WHERE num = prev_1 AND num = prev_2;

"""
