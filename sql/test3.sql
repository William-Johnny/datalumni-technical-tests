SELECT user_id as "Misssing user ID"
FROM "order"
WHERE NOT EXISTS (SELECT * 
                  FROM "user"
                  WHERE "user".id = "order".user_id ) GROUP BY user_id ;