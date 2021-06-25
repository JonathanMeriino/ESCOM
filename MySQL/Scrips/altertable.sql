-- agregar ka kkave primaria en la tabla detalleVenta siendo la PK el campo id
ALTER TABLE bdtemporal.detalleventa
ADD PRIMARY KEY(id);

DESC detalleventa;
-- agregar la llave foranea que pertenecen a los campos idClientes y idProductos en la tabla detalleVenta
ALTER TABLE detalleventa
ADD
  CONSTRAINT fkDetalleVentaProductos
  FOREIGN KEY (idProductos)
  REFERENCES productos(id)
  ON DELETE NO ACTION; 
  
ALTER TABLE bdtemporal.detalleventa
ADD
  CONSTRAINT fkDetalleVentaClientes
  FOREIGN KEY (idClientes)
  REFERENCES clientes(id)
  ON DELETE CASCADE;
  
  -- Borrar la llave primaria de la tabla detalleVenta
 ALTER TABLE detalleventa
  DROP PRIMARY KEY;
  
  -- Borrar la llave foranea de la tabla detalleVenta
   ALTER TABLE detalleventa
  DROP FOREIGN KEY fkDetalleVentaClientes;
  
  -- Borrar las llaves foraneas de la tabla detalle venta
  ALTER TABLE detalleventa
  DROP FOREIGN KEY fkDetalleVentaProductos;
  
  DESC detalleventa;
  
  
  
  
  
  
  
  
  
  
  
  