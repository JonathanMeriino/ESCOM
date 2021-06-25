USE test;
-- crear una tabla con constraint a nivel columna (primary key) o unique
CREATE TABLE clientes
(
id INT PRIMARY KEY AUTO_INCREMENT,
nombreCliente VARCHAR(30) NOT NULL UNIQUE,
ciudad VARCHAR(30),
telefono VARCHAR(30)
);
-- crear tabla con constraint a nivel de tabla
CREATE TABLE clientes1
(
id INT AUTO_INCREMENT,
nombreCliente VARCHAR(30) NOT NULL,
ciudad VARCHAR(30),
telefono VARCHAR(30),
CONSTRAINT cliente_pk PRIMARY KEY(id),
CONSTRAINT nombreCliente_UQ UNIQUE (nombreCliente)
);