CREATE TABLE empleado
(rut INT not null
,nombre TEXT
,cargo TEXT
,genero TEXT
,sueldo TEXT
,fk_id_local INT not null
,PRIMARY KEY (rut)
,FOREIGN KEY (fk_id_local) REFERENCES local(id_local));

CREATE TABLE local
(id_local INT not null
,nombre_l TEXT
,direccion TEXT
,fk_id_ciudad INT not null
,PRIMARY KEY (id_local)
,FOREIGN KEY (fk_id_ciudad) REFERENCES ciudad(id_ciudad));

CREATE TABLE ciudad
(id_ciudad INT not null
,nombre_c TEXT
,fk_id_region INT not null
,PRIMARY KEY (id_ciudad)
,FOREIGN KEY (fk_id_region) REFERENCES region(id_region));

CREATE TABLE region
(id_region INT not null
,nombre_c TEXT
,PRIMARY KEY (id_region));

INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);
INSERT INTO empleado values(12345678-9,Carlos Perez,auxiliar,hombre,230000,1);