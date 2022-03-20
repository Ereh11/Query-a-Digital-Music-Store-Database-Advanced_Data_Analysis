SELECT Gn.Name, COUNT(T.TrackId) as NumberOf_Tracks
FROM Genre AS Gn
INNER JOIN Track AS T
on T.GenreId= Gn.GenreId
GROUP BY Gn.Name
ORDER BY NumberOf_Tracks DESC;