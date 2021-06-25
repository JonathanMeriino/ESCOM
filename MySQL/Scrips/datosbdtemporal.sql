-- insertando 5 clientes en la tabla clientes
INSERT INTO clientes(id,nombreCliente,ciudad,telefono) VALUES(1,'Jonathan','Mexico','1234');
INSERT INTO clientes(id,nombreCliente,ciudad,telefono) VALUES(2,'Tania','Mexico','2345');
INSERT INTO clientes(id,nombreCliente,ciudad,telefono) VALUES(3,'Marco','Mexico','3456');
INSERT INTO clientes(id,nombreCliente,ciudad,telefono) VALUES(4,'Jessica','Mexico','4567');
INSERT INTO clientes(id,nombreCliente,ciudad,telefono) VALUES(5,'Alejandro','Mexico','5678');

-- insertando 3 productos en la tabla productos
INSERT INTO productos(id,nombreProducto,costo,precioVenta,existencia) VALUES(1,'Teclado gamer',100,130,5);
INSERT INTO productos(id,nombreProducto,costo,precioVenta,existencia) VALUES(2,'Mouse gamer',120,170,6);
INSERT INTO productos(id,nombreProducto,costo,precioVenta,existencia) VALUES(3,'Silla gamer',1000,1300,2);

-- insertando 1 venta de dos productos para el cliente 1

INSERT INTO detalleVenta(id,fechaVenta,idClientes,idProductos,cantidadVendida,costo,precioVenta)
				VALUES(1,'2019-12-31',1,1,2,100,130);
                
INSERT INTO detalleVenta(id,fechaVenta,idClientes,idProductos,cantidadVendida,costo,precioVenta)
				VALUES(2,'2019-12-31',1,2,1,120,170);
                
-- insert que viola la integridad referencial por que el cliente que quiero insertar no existe
INSERT INTO detalleVenta(id,fechaVenta,idClientes,idProductos,cantidadVendida,costo,precioVenta)
				VALUES(3,'2019-12-31',3,3,1,120,170);

SELECT * FROM detalleventa; 

DELETE FROM clientes
WHERE id=1;


