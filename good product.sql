SELECT DISTINCT product_name
FROM Products;

SELECT Products.product_id, Products.product_name, Products.price
FROM Products
INNER JOIN NutritionalInformation ON Products.product_id=NutritionalInformation.product_id
WHERE fiber > 5.00

SELECT Products.product_name
FROM Products
INNER JOIN NutritionalInformation ON Products.product_id=NutritionalInformation.product_id
WHERE protein = (
SELECT MAX(protein)
	FROM NutritionalInformation
)

SELECT Products.category_id, SUM(Products.calories) AS total_calories
FROM Products
INNER JOIN NutritionalInformation ON Products.product_id=NutritionalInformation.product_id
WHERE fat != 0
GROUP BY Products.category_id

SELECT Categories.category_name, ROUND(AVG(Products.price), 2) AS average_price
FROM Products
INNER JOIN Categories ON Products.category_id=Categories.category_id
GROUP BY Categories.category_name
