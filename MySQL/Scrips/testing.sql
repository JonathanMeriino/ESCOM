SELECT CURRENT_DATE();

SELECT CURRENT_DATE(), DATE_FORMAT(CURRENT_DATE(),'%m / %d / %y ');
SELECT CURRENT_DATE(), DATE_FORMAT(CURRENT_DATE(),'%M / %D / %Y ');

SELECT "hola mundo", CONCAT("hola mundo","ho es un buen dia");

SELECT "hola mundo" as cadena1, CONCAT("hola mundo","ho es un buen dia") as cadena2;
SELECT "hola mundo" as cadena1, LEFT(CONCAT("hola mundo","ho es un buen dia") ,10)as cadena2;
SELECT SUM(10+15) as suma, ROUND (154.694,2) AS redondeado;