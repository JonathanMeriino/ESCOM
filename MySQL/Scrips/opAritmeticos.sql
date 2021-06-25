-- realizamos una consulta de la tabla entradaSalidaDinero analizando in ingreso-egreso con id= 21
-- para hacer uso del modulo y residuo
SELECT idIngresosEgresos, montoIE/2 as "divisionDos",
montoIE DIV 2 AS "parteEntera", montoIE MOD 3 as "Residuo"
FROM entradasalidadinero
WHERE id = 21;
-- hacemos uso de parentesis en operacion aritmetica para demostrar la presencia
SELECT idIngresosEgresos,montoIE, montoIE + 2 *3 AS "Sin parentesis",
(montoIE +2)*3 AS "conParentesis"
FROM entradasalidadinero
WHERE id= 21;