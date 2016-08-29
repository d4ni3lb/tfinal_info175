SELECT nombre_l AS Local ,ciudad.nombre_c AS Ciudad ,local.direccion, COUNT(nombre) AS Total_empleado FROM local ,empleado join ciudad  on local.fk_id_ciudad = ciudad.id_ciudad and  empleado.fk_id_local = local.id_local GROUP BY nombre_l;
	
/*SELECT COUNT(nombre) AS Total_empleado,local.nombre_l FROM empleado JOIN local  WHERE empleado.fk_id_local = local.id_local GROUP BY nombre_l;*/

/*select nombre from empleado;*/

/*SELECT COUNT(genero) AS Total_Por_genero,genero from empleado GROUP BY genero;*/

/*SELECT SUM(sueldo) AS Total_Sueldo_Por_local,local.nombre_l FROM empleado JOIN local where empleado.fk_id_local= local.id_local group by nombre_l;*/

/*SELECT local.nombre_l,region.nombre_c AS Nombre_Region from  local,ciudad join region where ciudad.fk_id_region = region.id_region AND local.fk_id_ciudad = ciudad.id_ciudad; */

INSERT INTO empleado(rut,nombre,cargo,genero,sueldo,fk_id_local) Values (12312323,"Armando Este Banquito", "Cajero","Masculino",180000,4);