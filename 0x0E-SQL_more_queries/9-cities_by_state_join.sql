-- lists all the cities in hbtn_0d_usa
SELECT cities.id, cities.name, states.name
INNER JOIN states ON cities.state_id = states.id
FROM cities
ORDER BY cities.id ASC;
