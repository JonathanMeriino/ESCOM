SELECT * FROM personas
WHERE id != 8;

SELECT * FROM entradasalidadinero
WHERE fechaES= "2018-01-01";

SELECT * FROM entradasalidadinero
WHERE (montoIE/2) <1000;

SELECT *, LEFT (nombre,1)
FROM personas
WHERE LEFT(nombre,1)<'K';

SELECT * FROM personas
WHERE id!=8 AND LEFT(telefono,3)='493'
AND id MOD 2= 0;

SELECT * FROM personas
WHERE LEFT(telefono,3)='493' OR LEFT (telefono,3) ='444';

SELECT * FROM personas
WHERE NOT LEFT(telefono,3)='493';

SELECT * FROM entradasalidadinero
WHERE NOT (montoIE>=5000 OR NOT fechaES<='2018/12/31');

SELECT * FROM entradasalidadinero
WHERE montoIE>=5000 AND fechaES<='2018/12/31';

SELECT * FROM personas
WHERE id= 8 OR id=10 OR id= 3 and id =4;

SELECT * FROM personas
WHERE (id= 8 OR id=10 OR id= 3) and (id =4);

SELECT * FROM personas
WHERE NOT(id= 8 OR id=10 OR id= 3) and (id =4);
