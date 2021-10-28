var getData = function(){
    var nombre = document.getElementById("nombre").value;
    var paterno = document.getElementById("paterno").value;
    var materno = document.getElementById("materno").value;

    var calle = document.getElementById("calle").value;
    var numero = document.getElementById("numero").value;
    var colonia = document.getElementById("colonia").value;
    var cp = document.getElementById("cp").value;
    var ciudad = document.getElementById("ciudad").value;

    var sexo = document.getElementById("sexo").value;
    var nacimiento = document.getElementById("nacimiento").value;
    var curp = document.getElementById("curp").value;

    var programacion = document.getElementById("programacion").value;

    var comentarios = document.getElementById("comentarios").value;
    document.write(nombre+" "+paterno+" "+materno+"\n");

    document.write(calle+" "+numero+" "+colonia+" "+cp+" "+ciudad+"\n");

    document.write(sexo+" "+nacimiento+" "+curp+"\n");

    document.write(programacion+" ")

    document.write(comentarios+" ");
}