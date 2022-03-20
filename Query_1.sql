SELECT Gn.Name, SUM(Vn.UnitPrice * Vn.Quantity) AS total_Purchases 
FROM Genre AS Gn
JOIN Track AS Tc ON Gn.GenreId = Tc.GenreId
JOIN InvoiceLine AS Vn ON Tc.TrackId = Vn.TrackId
GROUP BY Gn.Name
ORDER BY total_Purchases DESC;