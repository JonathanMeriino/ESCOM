USE bdtemporal;
-- mostrar estructura de la tabla productos 
DESC productos;
-- agregar una columna a la tabla de productos llamada color
ALTER TABLE productos
ADD color VARCHAR(20);
-- agregar una columna llamada coloar a la tabla de productos despues del campo costo
ALTER TABLE productos
ADD color VARCHAR(20) AFTER costo;
-- agregar una columna a la tabla de productos siendo el primer campo de la definicion ddl
ALTER TABLE productos
ADD color VARCHAR(20) FIRST;
-- Borrar un campo de la tabla productos, la existencia (no se puede borrar algun campo que viole
-- la integridad referencial
ALTER TABLE productos
DROP COLUMN existencia; 
-- cambiar el tamaño de una columna(nombreProducto), no te dejara cambiarlo si violas el tamaño de los 
-- registros que ya tengan informacion
ALTER TABLE productos 
MODIFY nombreProducto VARCHAR(50) NOT NULL;
-- cambiar el tipo de dato de una columna, no te permitira hacer el cambio 
-- si tu campo no acepta el tipo de dato con los datos que ya se tenian almacenados
ALTER TABLE productos
MODIFY nombreProducto CHAR(50) NULL;
-- cambiar el valor default para un registro cuando se interte
ALTER TABLE productos
MODIFY nombreProducto CHAR(50) NULL DEFAULT 'coloqueNombreDelProducto';
-- cambiar el valor default para un registro cuando se inserte
ALTER TABLE productos
CHANGE COLUMN costo precioCompra decimal(8,2);











