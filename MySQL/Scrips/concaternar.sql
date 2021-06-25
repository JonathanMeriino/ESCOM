-- realiza un ejemplo con la tabla personas en la cual concatenas tres campos y una funcion propia de mysql
-- ademas utiliza las apostrofes dentro de la cadena para demostrar como se utilizan

SELECT *,concat(nombre,' "con correo:" ',correo, '"con fecha: " ',now()) as "CampoContaneado"
FROM personas