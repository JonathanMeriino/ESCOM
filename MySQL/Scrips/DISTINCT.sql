-- Distinct sacar los renglones distintos en una consulta SQL
SELECT DISTINCT fechaES
FROM entradasalidadinero;


SELECT COUNT(DISTINCT fechaES)
FROM entradasalidadinero;

SELECT DISTINCT YEAR (fechaES)
FROM entradasalidadinero;

SELECT DISTINCT (idestatuspendiente) FROM pendientes;

SELECT COUNT(DISTINCT idpersonas)
FROM entradasalidadinero;


SELECT DISTINCT (idpersonas) FROM entradasalidadinero;