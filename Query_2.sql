SELECT Ar.Name, SUM(Vn.UnitPrice * Vn.Quantity) AS Total_Purchase_Rock 
FROM Artist AS Ar
JOIN Album AS Ab ON Ar.ArtistId = Ab.ArtistId
JOIN Track AS Tc ON Ab.AlbumId = Tc.AlbumId
JOIN InvoiceLine AS Vn ON Tc.TrackId = Vn.TrackId
JOIN Genre AS Gn ON Tc.GenreId = Gn.GenreId
WHERE Gn.Name = 'Rock'
GROUP BY Ar.Name
ORDER BY Total_Purchase_Rock DESC
LIMIT 10;