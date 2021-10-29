var getData = function(){
    
    let form = document.forms["myForm"];
    
    let nombre = form.nombre.value;
    let paterno = form.paterno.value;
    let materno = form.materno.value;

    let calle = form.calle.value;
    let numero = form.numero.value;
    let colonia = form.colonia.value;
    let cp = form.cp.value;
    let ciudad = form.ciudad.value;

    let sexo = form.sexo.value;
    let nacimiento = form.nacimiento.value;
    let curp = form.curp.value;

    let programacion = document.getElementsByName("programacion[]");
    let hobbies = document.getElementsByName("hobbies[]");

    var comentarios = document.getElementById("comentarios").value;
    document.write("Nombre: "+nombre+
                    "<br> Apellido Paterno: "+paterno+
                    "<br> Apellido Materno "+materno);

    document.write("<br> Calle: "+calle+
                    "<br> Numero: "+numero+
                    "<br> Colonia: "+colonia+
                    "<br> Codigo Postal: "+cp+
                    "<br> Ciudad "+ciudad);

    document.write("<br> Sexo: "+sexo+
                    "<br> Nacimiento: "+nacimiento+
                    "<br> CURP: "+curp);

    let mensajeProgra = "Lenguajes de programacion: ";
    
    for(let i =0;i<programacion.length; i++){
        const element = programacion[i];
        if(element.checked){
            mensajeProgra+=element.value+" ";
        }
        
    }
    
    let mensajeHobbies = "Hobbies: ";
    for(let i=0; i<hobbies.length; i++){
        const element = hobbies[i];
        if(element.checked){
            mensajeHobbies+=element.value+" ";
        }
    }
    
    document.write("<br> Lenguajes de programacion: C , C++, Java, Python");
    document.write("<br> Hobbies: Leer, Videojuegos, Ver Netflix");
    document.write("<br> Comentarios: Ninguno");

    


}