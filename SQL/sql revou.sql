SELECT 
    "Discount" AS Tingkat_Diskon,
    COUNT("Order ID") AS Total_Transaksi,
    ROUND(AVG("Profit Margin"), 2) AS Avg_Profit_Margin_Percent
FROM "RevoU Dataset"
GROUP BY Discount
ORDER BY Discount ASC;

SELECT 
    "Sub-Category" AS Sub_Kategori,
    ROUND(SUM(CAST(REPLACE(REPLACE("Sales", '"', ''), ',', '') AS FLOAT)), 0) AS Total_Sales,
    ROUND(SUM(CAST(REPLACE(REPLACE("Profit", '"', ''), ',', '') AS FLOAT)), 0) AS Total_Profit
FROM "RevoU Dataset"
GROUP BY "Sub-Category"
ORDER BY Total_Sales DESC;


SELECT 
    "Sub-Category" AS Sub_Kategori,
    ROUND(AVG(Discount) * 100, 2) AS Average_Discount_Percent,
    ROUND(SUM(CAST(REPLACE(REPLACE("Profit", '"', ''), ',', '') AS FLOAT)), 0) AS Total_Profit_Loss
FROM "RevoU Dataset"
WHERE "Sub-Category" IN ('Tables', 'Bookcases', 'Supplies', 'Fasteners')
GROUP BY "Sub-Category"
ORDER BY Average_Discount_Percent DESC;

SELECT 
    "Segment",
    ROUND(AVG(Discount) * 100, 2) AS Avg_Discount_Percent,
    ROUND(SUM(CAST(REPLACE(REPLACE("Profit", '"', ''), ',', '') AS FLOAT)), 0) AS Total_Profit,
    ROUND(SUM(CAST(REPLACE(REPLACE("Sales", '"', ''), ',', '') AS FLOAT)), 0) AS Total_Sales,
    ROUND((SUM(CAST(REPLACE(REPLACE("Profit", '"', ''), ',', '') AS FLOAT)) / 
           SUM(CAST(REPLACE(REPLACE("Sales", '"', ''), ',', '') AS FLOAT))) * 100, 2) AS Profit_Margin_Percent
FROM "RevoU Dataset"
GROUP BY "Segment"
ORDER BY Total_Profit DESC;