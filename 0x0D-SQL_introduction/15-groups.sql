SELECT score, COUNT(1) AS number FROM second_table
--script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
GROUP BY score
ORDER BY number DESC;
