-- Sentencia SQL que regresa todos los registros de la tabla personas
SELECT * FROM personas;

-- Regresa los campos nombre y correo de la tabla persona por cada renglon y los ordena de forma descendente por nombre
SELECT nombre,correo
FROM personas
ORDER BY nombre DESC;

-- Regresa fecha de entrada o salida de dinero, el monto de entrada o salida 
-- de la tabla entradaSalidaDinero, donde la fecha este entre el 1 de enero de 2018 y 31 de enero del mismo año
-- ordenados de forma ascendente

SELECT fechaES,montoIE 
FROM entradaSalidaDinero
WHERE fechaES BETWEEN '2018/01/01' and '2018/01/31'
ORDER BY fechaES ASC;

-- Regresa los registros de la tabla entradaSalidaDinero cuyo monto sea mayor o igual a 500,
-- y ese monto se muestra multiplicando por 2, solamente muestra los campos id, fechaES
SELECT id, fechaES,montoIE*2 as "multiploPor2"
FROM entradaSalidaDinero
WHERE montoIE >=500















