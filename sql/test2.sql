SELECT 
    strftime('%Y', order_received) AS Year,
    SUM(id) as "Order count",
    COUNT(order_received) as "Line count"
FROM "order" GROUP BY Year;