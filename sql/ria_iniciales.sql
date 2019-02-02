CREATE DATABASE ria_iniciales;
USE ria_iniciales;

CREATE TABLE clientes(
  id int(4) AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(50) NOT NULL,
  apellidos varchar(50) NOT NULL,
  correo varchar(55) NOT NULL,
  telefono varchar(10) NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos(
  codigo int(4) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre varchar(40) NOT NULL,
  marca varchar(25) NOT NULL,
  categoria varchar(50) NOT NULL,
  precio float(6,2) UNSIGNED NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(nombre, apellidos, correo, telefono) VALUES
  ('Mario Alberto','Nieto Lopez', 'manl_19@email','7757544415'),
  ('Luis Ernesto', 'Calderon Orozco', 'luis_CO@gmail','7757423672'),
  ('Ximena','Arteaga Granillo','XimenA@email','7757427175');

INSERT INTO productos(nombre, marca, categoria,precio) VALUES
  ('Carlos V','NESTLE','dulces',12.0),
  ('Uncanny AVENGERS','MARVEL','comics',24.5),
  ('XBOX: THE DIVISION','UBISOFT','videojuegos',899.99);

SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
