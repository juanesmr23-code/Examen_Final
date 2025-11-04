CREATE DATABASE IF NOT EXISTS greengrowth;
USE greengrowth;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    nombre VARCHAR(100)
);

CREATE TABLE invernaderos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    superficie DECIMAL(10,2),
    tipo_cultivo VARCHAR(50),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    responsable VARCHAR(100),
    capacidad_ton DECIMAL(10,2),
    sistema_riego ENUM('manual','automatizado','goteo'),
    estado ENUM('Operativo','Reparación','Inspección','Expansión') DEFAULT 'Operativo'
);

CREATE TABLE enfermedades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    gravedad VARCHAR(20),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

