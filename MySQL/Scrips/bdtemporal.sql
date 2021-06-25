-- borramos la base de datos
drop database if exists bdTemporal;

-- creamos la base de datos
create database if not exists bdTemporal;

-- seleccionamos la base de datos
use bdTemporal;

-- crear una tabla que no tenga ningun atributo
CREATE TABLE clientes
(
  id int primary key auto_increment,
  nombreCliente varchar(30) not null unique,
  ciudad varchar (30),
  telefono varchar(30)
)ENGINE = InnoDB;
-- crear una tabla que tenga atributos en sus columnas y defina el nombre de la base de datos
CREATE TABLE IF NOT EXISTS bdTemporal.productos
(
  id int  primary key not null     unique       auto_increment     ,
  nombreProducto varchar(30)   unique,
  costo decimal(8,2)           not null    default 0,
  precioVenta decimal(8,2)     not null    default 0,
  existencia decimal(8,2)      not null    default 0
)ENGINE = InnoDB;

-- creamos la tabla 
CREATE TABLE IF NOT EXISTS detalleVenta
(
   id int primary key not null     unique       auto_increment     ,
fechaVenta date not null,
  idClientes int not null,
  idProductos int not null,
  cantidadVendida decimal(8,2) not null,
  costo decimal(8,2)      not null    default 0,
  precioVenta decimal (8,2)not null,
 
 CONSTRAINT fkDetalleVentaProductos
  FOREIGN KEY (idProductos)
  REFERENCES productos(id)
  ON DELETE NO ACTION,
  
   CONSTRAINT fkDetalleVentaClientes
  FOREIGN KEY (idClientes)
  REFERENCES clientes(id)
  ON DELETE CASCADE
  
)ENGINE = InnoDB;
