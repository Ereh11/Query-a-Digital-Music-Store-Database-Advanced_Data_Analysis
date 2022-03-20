SELECT Ab.Title, COUNT(Tc.TrackId) AS NumberTrack_forEachAlbum
FROM Album as Ab
JOIN Track as Tc on Ab.AlbumId = Tc.AlbumId
GROUP BY Ab.Title
ORDER BY NumberTrack_forEachAlbum DESC
LIMIT 20;