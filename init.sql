CREATE TABLE IF NOT EXISTS points_of_interest (
    id INTEGER PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    tipo_POI VARCHAR
);

COPY points_of_interest
FROM '/home/pois.csv'
DELIMITER ','
CSV HEADER;
