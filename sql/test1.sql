SELECT 
	order_line.id as "Order ID",
	CONCAT("order".order_received,' ',"order".payment_received,' ',"order".order_prepared,' ',"order".order_shipped,' ',"order".order_delivered) as "Order Status",
	"user".id as "User ID",
	CONCAT("user".first_name,' ', "user".last_name) as "Full name"
FROM 
	order_line 
	JOIN "order" ON order_line.order_id="order".id JOIN "user" ON "order".user_id="user".id
	WHERE "Order ID">1337 AND "Order ID"<=1500
	ORDER BY last_name DESC;