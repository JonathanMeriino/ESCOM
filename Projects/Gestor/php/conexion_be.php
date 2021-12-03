<?php
    $conexion = mysqli_connect("localhost","root","","login_registro");

    if($conexion ){
        echo 'Conectado exitosamente';
    }else{
        echo 'No se ha podido conectar';
    }



?>