SELECT 
    "user".id AS "User ID",
    CONCAT("user".first_name,' ', "user".last_name) AS "Full name",
    SUM(CASE WHEN strftime('%Y', order_received) = "2018" THEN order_line.unit_price * order_line.quantity ELSE 0 END) AS "Rank 2018",
    SUM(CASE WHEN strftime('%Y', order_received) = "2019" THEN order_line.unit_price * order_line.quantity ELSE 0 END) AS "Rank 2019"
FROM "user"
    JOIN "order" ON "user".id = "order".user_id 
    JOIN order_line ON "order".id = order_line.order_id 
	WHERE strftime('%Y', order_received) = "2018" OR  strftime('%Y', order_received) = "2019"
	GROUP BY"user".id, "Full name"
	ORDER BY "Rank 2018" DESC
	LIMIT 10;
