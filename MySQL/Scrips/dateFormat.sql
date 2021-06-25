-- Hacer uso de las tres funciones antes explicadas, dar formato a campo de fecha
-- extraer los 10 primeros caracteres de una campo de base de datos llamado observaciones y por ultimo
-- redondear un dato numerico en tres diferentes formatos con informacion de la tabla entradaSalidaDinero

SELECT id,fechaES,date_format(fechaES,'%d/%m/%y') AS 'fecha1',date_format(fechaES,'%e-%b-%y') AS 'fecha2'
from entradasalidadinero
WHERE id>500;