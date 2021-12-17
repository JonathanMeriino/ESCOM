

function start(e) {
    e.dataTransfer.effecAllowed = 'move'; // Define el efecto como mover
    e.dataTransfer.setData("Data", e.target.id); // Coje el elemento que se va a mover
    e.dataTransfer.setDragImage(e.target, 0, 0); // Define la imagen que se vera al ser arrastrado el elemento y por donde se coje el elemento que se va a mover (el raton aparece en la esquina sup_izq con 0,0)
    e.target.style.opacity = '0.4'; // Establece la opacidad del elemento que se va arrastrar
}
function end(e) {
    e.target.style.opacity = ''; // Restaura la opacidad del elemento   
    e.dataTransfer.clearData("Data");
}
function enter(e) {
    e.target.style.border = '3px dotted #555'; 
}

function leave(e) {
    e.target.style.border = ''; 
}
function over(e) {
    var elemArrastrable = e.dataTransfer.getData("Data"); // Elemento arrastrado
    var id = e.target.id; // Elemento sobre el que se arrastra
    
    // return false para que se pueda soltar
    if (id == 'panelEdicion') {
        return false; // Cualquier elemento se puede soltar sobre el div destino 1
    }
    if (id == 'papelera') {
        return false; // Cualquier elemento se puede soltar en la papelera
    }  

  
}
//funcion que hace que los elementos se situen exactamente en donde se sueltan
function drop(e) {
    var elementoArrastrado = e.dataTransfer.getData("Data"); // Elemento arrastrado
   
    e.target.appendChild(document.getElementById(elementoArrastrado)); // Añade el elemento arrastrado al elemento desde el que se llama a esta funcion

  

    // Posicion absoluta del raton
    x = e.layerX;
    y = e.layerY;

  

    document.getElementById(elementoArrastrado).style.position="absolute";
    document.getElementById(elementoArrastrado).style.left=x+"px";
    document.getElementById(elementoArrastrado).style.top=y+"px";
    e.target.style.border = '';   // Quita el borde del cuadro al que se mueve
}


function agregaText(id) {
    var elemento =document.getElementById(id);
   
    var valor = prompt("Que deseas ingresar en "+id, "Sin valor");
    elemento.insertAdjacentHTML("beforeend","<text x='70' y='70'>"+valor+"</text>");
}
function agregaText2(id, text) {
    var elemento =document.getElementById(id);
   
  
    elemento.insertAdjacentHTML("beforeend","<text x='70' y='70'>"+text+"</text>");
}
var contador = 0;
function inicio() {
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
 panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idBegin"+contador+"' width='205px' onclick='agregaText(this.id)' height='170px'><rect class='color' x='2' y='2' rx='200' ry='120' width='200px' height='120px'style=' fill: white; stroke:black; stroke-width: 2px;' /><line class='color' x1='100' y1='130' x2='100' y2='160' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='90' y2='150' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='110' y2='150' style='stroke:navy;stroke-width:2'/></svg></div>");
 textContent = document.getElementById('codigo');
            espacio=document.createElement('div');//se crea
            textContent.appendChild(espacio);
            espacio.innerHTML = '<p>int main(){ <br />';
}

function declaracionVariables() {
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idvaria"+contador+"' onclick='agregaText(this.id)' width='205px' height='170px'><rect class='color' x='2' y='2' rx='15' ry='15' width='200px' height='20px'style=' fill: white; stroke:black; stroke-width: 2px;' /><rect class='color' x='2' y='22' rx='10' ry='10' width='200px' height='100px'style=' fill: white; stroke:black; stroke-width: 2px;' /><rect class='color' x='2' y='112' rx='15' ry='15' width='200px' height='20px'style=' fill: white; stroke:black; stroke-width: 2px;' /><line class='color' x1='100' y1='130' x2='100' y2='160' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='90' y2='150' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='110' y2='150' style='stroke:navy;stroke-width:2'/></svg></div>");
    var id = "idvaria"+contador;
    var tipo = prompt("ingresa el tipo de dato de tu variabble");
    texto = prompt('Ingresa el nombre de tu variable:');
    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');//se crea
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>&nbsp;&nbsp;'+tipo+'&nbsp;'+texto+';<br />';
    agregaText2(id,texto);
}

function entradaDatos() {
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='identradadato"+contador+"' onclick='agregaText(this.id)' width=185 height=170> <path class='color' d='M 5 120 Q 75 78 90 120 T 180 120  M 180 280 z'stroke='navy' stroke-width=2 fill='white' /><line class='color' x1='5' y1='5' x2='5' y2='120' style='stroke:navy;stroke-width:2'/><line class='color' x1='5' y1='5' x2='180' y2='5' style='stroke:navy;stroke-width:2'/><line class='color' x1='180' y1='5' x2='180' y2='120' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='140' x2='100' y2='160' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='90' y2='150' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='110' y2='150' style='stroke:navy;stroke-width:2'/></svg></div>");
    var id = "identradadato"+contador;
    texto = prompt('Ingresa la variable de entrada:');
    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>&nbsp;&nbsp;scanf("%d",&'+texto+');<br />';
    agregaText2(id,texto);


}
function salidaDatos(){
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idsalidadato"+contador+"' onclick='agregaText(this.id)' width=200 height=185><polygon class='color' points='10,140 10,50 40,10 190,10 190,140 ' style='fill:white;stroke:navy;stroke-width:2' /><line class='color' x1='100' y1='150' x2='100' y2='180' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='180' x2='90' y2='170' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='180' x2='110' y2='170' style='stroke:navy;stroke-width:2'/></svg></div>");
    var id = "idsalidadato"+contador;
    texto = prompt('Ingresa tu salida :')
            textContent = document.getElementById('codigo');
            espacio=document.createElement('div');//se crea
            textContent.appendChild(espacio);
            espacio.innerHTML = '<p>&nbsp;&nbsp;printf("'+texto+'");<br />';
           
            agregaText2(id,texto);
}
function sentenciaSimple(){
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idsentenciasimple"+contador+"' onclick='agregaText(this.id)' width='205px' height='180px'><rect class='color' x='2' y='2' width='200px' height='120px'style=' fill: white; stroke:black; stroke-width: 2px;' /><line class='color' x1='100' y1='130' x2='100' y2='160' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='90' y2='150' style='stroke:navy;stroke-width:2'/><line class='color' x1='100' y1='160' x2='110' y2='150' style='stroke:navy;stroke-width:2'/></svg></div>");
    var id = "idsentenciasimple"+contador;
    texto = prompt('Ingresa tu entrada de dato:')
    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');//se crea
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>&nbsp;&nbsp;'+texto+';<br />';
    agregaText2(id,texto);
}
function condicional(){
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    //panel.insertAdjacentHTML("beforeend"," <div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idcondicion"+contador+"' onclick='agregaText(this.id)' width='150px' height='150px'><polygon class='color' points='0,75 75,0 150,75 75,150' style='fill:white;stroke:navy;stroke-width:2' /></svg></div>");
   // tabla=document.getElementById('tabla1');
   // fila=document.createElement('tr');//se crea
   // tabla.appendChild(fila);
  //  div=document.createElement('div');//se crea
    condicion = prompt('Ingresa tu condición:')
    instruccion1 = prompt('Ingresa tu instruccion en caso de no cumplir:')
    instruccion2 = prompt('Ingresa tu instruccion en caso de si cumplir:')
    panel.insertAdjacentHTML('beforeend','<div class="esp" id="div'+contador+'"draggable="true" ondragstart="start(event)" ondragend="end(event)"><svg width="315" height="250">'+
    '<polygon points="65 30, 110 60, 160 30, 110 2" class="figuraIF color"/>'+
    '<text x="80"  y="35" class="textos">'+condicion+'</text>'+
    '<text x="160"  y="25" >NO</text>'+
    '<text x="120"  y="70" >SI</text>'+
    '<rect  x="50" y="125"  width="110" height="60" class="figura color"/>'+
    '<text x="60"  y="155" class="textos">'+instruccion2+'</text>'+
    '<rect x="200" y="125"  width="110" height="60" class="figura color"/>'+
    '<text x="210"  y="155" class="textos">'+instruccion1+'</text>'+
    '<rect x="110" y="60"  width="2" height="50" class="contornoIF"/>'+
    '<polygon  points="102 105,122 105,112 120" class="contornoIF"/>'+
    '<rect  x="160" y="28"  width="90" height="2" class="contornoIF"/>'+
    '<rect x="250" y="28"  width="2" height="88" class="contornoIF"/>'+
    '<polygon  points="242 105,262 105,252 120" class="contornoIF"/>'+
    '<rect x="110" y="186"  width="2" height="50" class="flecha"/>'+
    '<polygon  points="102 235,122 235,112 250" class="flecha"/>'+
    '<rect x="250" y="186"  width="2" height="30" class="flecha"/>'+
    '<rect x="110" y="215"  width="145" height="2" class="flecha"/>'+
    '</svg></div>');
    //fila.appendChild(div);

    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');//se crea
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>&nbsp;&nbsp;if ('+condicion+'){<br />'+
                        '<p>&nbsp;&nbsp;&nbsp;'+instruccion2+';'+
                        '<p>&nbsp;&nbsp;}else{'+
                        '<p>&nbsp;&nbsp;&nbsp;'+instruccion1+';'+
                        '<p>&nbsp;&nbsp;}';
}
function repeticion(){
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
    //panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idrepeticion"+contador+"' onclick='agregaText(this.id)' width='150px' height='150px'><polygon class='color' points='0,75 75,0 150,75 75,150' style='fill:white;stroke:navy;stroke-width:2' /></svg></div>");
    inicializacion = prompt('Ingresa tu inicialización:')
    condicion = prompt('Ingresa tu condicion:')
    incremento = prompt('Ingresa tu incremento o decremento:')
    texto1 = prompt('Ingresa tu instruccion para caso SI :')
    texto2 = prompt('Ingresa tu instruccion para caso NO :')
    div=document.createElement('div');//se crea
    panel.insertAdjacentHTML('beforeend','<div class="esp" id="div'+contador+'"draggable="true" ondragstart="start(event)" ondragend="end(event)"><svg width="210" height="645">'+
    '<rect x="50" y="5"  width="110" height="60" class="figura color"/>'+
    '<text x="60"  y="35" class="textos">'+inicializacion+'</text>'+
    '<rect x="100" y="65"  width="5" height="50" class="flecha"/>'+
    '<polygon points="92 110,112 110,102 120" class="flecha"/>'+

    '<polygon points="55 150, 100 180, 150 150, 100 120" class="figuraIF color"/>'+
    '<text x="75"  y="155" class="textos">'+condicion+'</text>'+
    '<rect x="100" y="180"  width="5" height="50" class="contornoIF"/>'+
    '<polygon points="92 230,112 230,102 240" class="contornoIF"/>'+
    '<rect x="150" y="147"  width="30" height="5" class="contornoIF"/>'+
    '<rect x="180" y="147"  width="5" height="330" class="contornoIF"/>'+
    '<rect x="100" y="477"  width="85" height="5" class="contornoIF"/>'+
    '<rect x="100" y="477"  width="5" height="35" class="contornoIF"/>'+
    '<polygon points="92 512,112 512,102 522" class="contornoIF"/>'+
    '<text x="160"  y="140" >NO</text>'+
    '<text x="110"  y="190" >SI</text>'+

    '<rect x="50" y="525"  width="110" height="60" class="figura color"/>'+
    '<text x="60"  y="555" class="textos">'+texto2+'</text>'+
    '<rect x="100" y="585"  width="5" height="50" class="flecha"/>'+
    '<polygon points="92 635,112 635,102 645" class="flecha"/>'+

    '<rect x="50" y="245"  width="110" height="60" class="figura color"/>'+
    '<text x="60"  y="270" class="textos">'+texto1+'</text>'+
    '<rect x="100" y="305"  width="5" height="50" class="flecha"/>'+
    '<polygon points="92 355,112 355,102 365" class="flecha"/>'+

    '<rect x="50" y="370"  width="110" height="60" class="figura color"/>'+
    '<text x="60"  y="400" class="textos">'+incremento+'</text>'+
    '<rect x="100" y="430"  width="5" height="30" class="flecha"/>'+
    '<rect x="30" y="460"  width="75" height="5" class="flecha"/>'+
    '<rect x="25" y="90"  width="5" height="375" class="flecha"/>'+
    '<rect x="30" y="90"  width="65" height="5" class="flecha"/>'+
    '<polygon points="90 82,90 102,100 92" class="flecha"/>'+
    '</svg></div>');
    //fila.appendChild(div);

    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');//se crea
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>&nbsp;&nbsp;for('+inicializacion+';'+condicion+';'+incremento+'){<br />'+
                        '<p>&nbsp;&nbsp;&nbsp;'+texto1+';'+
                        '<p>&nbsp;&nbsp;}'+
                        '<p>&nbsp;&nbsp;'+texto2+';';
}
function endSimbol(){
    contador = contador +1;
    var panel = document.getElementById("panelEdicion");
   
    panel.insertAdjacentHTML("beforeend","<div class='esp' id='div"+contador+"' draggable='true' ondragstart='start(event)' ondragend='end(event)'><svg id='idendSim"+contador+"' width='205px' onclick='agregaText(this.id)' height='125px'><rect class='color' x='2' y='2' rx='200' ry='120' width='200px' height='120px'style=' fill: white; stroke:red; stroke-width: 2px;' /></svg></div>");
    textContent = document.getElementById('codigo');
    espacio=document.createElement('div');//se crea
    textContent.appendChild(espacio);
    espacio.innerHTML = '<p>} <br />';
}
const url = "http://localhost:8000/api/save";
function save(){
    const diagrama = document.getElementById("panelEdicion");
    const codigo = document.getElementById("codigo").textContent;
    var name = document.getElementById("diagramaName");
    var html = diagrama.outerHTML;       
    var data = { html: html, nombre: name.value }; 
    var code = { code: codigo, nombre: name.value};

   

let data2 = {
  name: 'Sara'
};
(async () => {
    try {
        // en el objeto “datos” tenemos los datos que vamos a enviar al servidor
        // en este ejemplo tenemos dos datos; un título y un array de números
      //  var datos = { titulo: "Listado de números", numeros: [2,4,6,8,10] };
        // en el objeto init tenemos los parámetros de la petición AJAX
        var init = {
            // el método de envío de la información será POST
            method: "POST",
         
            headers: { // cabeceras HTTP
                // vamos a enviar los datos en formato JSON
                'Content-Type': 'application/json'
            },
            // el cuerpo de la petición es una cadena de texto
            // con los datos en formato JSON
            body: JSON.stringify(data) // convertimos el objeto a texto
        };
        // realizamos la petición AJAX usando fetch
        // el primer parámetro es el recurso del servidor al que queremos acceder
        // en este ejemplo, es un fichero php llamado media.php que se encuentra
        // dentro de la carpeta ./php y con el código PHP que hay arriba.
        // el segundo parámetro es el objeto init con la información sobre los
        // datos que queremos enviar, el método de envio, etc.
        var response = await fetch('http://localhost:8000/api/save', init);
        if (response.ok) {
         alert("Archivo "+name.value+" creado con exito");
        } else {
            throw new Error(response.statusText);
            
        }
    } catch (err) {
        console.log("Error al realizar la petición AJAX: " + err.message);
        alert("Error al crear por favor pongale un nombre al archivo");
    }
})();
// creacion del archivo c (parte que manda los datos al back)
(async () => {
    try {
        // en el objeto “datos” tenemos los datos que vamos a enviar al servidor
        // en este ejemplo tenemos dos datos; un título y un array de números
      //  var datos = { titulo: "Listado de números", numeros: [2,4,6,8,10] };
        // en el objeto init tenemos los parámetros de la petición AJAX
        var init = {
            // el método de envío de la información será POST
            method: "PUT",
         
            headers: { // cabeceras HTTP
                // vamos a enviar los datos en formato JSON
                'Content-Type': 'application/json'
            },
            // el cuerpo de la petición es una cadena de texto
            // con los datos en formato JSON
            body: JSON.stringify(code) // convertimos el objeto a texto
        };
        // realizamos la petición AJAX usando fetch
        // el primer parámetro es el recurso del servidor al que queremos acceder
        // en este ejemplo, es un fichero php llamado media.php que se encuentra
        // dentro de la carpeta ./php y con el código PHP que hay arriba.
        // el segundo parámetro es el objeto init con la información sobre los
        // datos que queremos enviar, el método de envio, etc.
        var response = await fetch('http://localhost:8000/api/upload', init);
        if (response.ok) {
         console.log(response);
        } else {
            throw new Error(response.statusText);
        }
    } catch (err) {
        console.log("Error al realizar la petición AJAX: " + err.message);
    }
})();

}
function upload(){
    var archivo = document.getElementById("file");
    //alert(archivo.value);
    let data2 = {
        name: archivo.value
      };
    (async () => {
        try {
            // en el objeto “datos” tenemos los datos que vamos a enviar al servidor
            // en este ejemplo tenemos dos datos; un título y un array de números
          //  var datos = { titulo: "Listado de números", numeros: [2,4,6,8,10] };
            // en el objeto init tenemos los parámetros de la petición AJAX
            var init = {
                // el método de envío de la información será POST
                method: "PUT",
             
                headers: { // cabeceras HTTP
                    // vamos a enviar los datos en formato JSON
                    'Content-Type': 'application/json'
                },
                // el cuerpo de la petición es una cadena de texto
                // con los datos en formato JSON
                body: JSON.stringify(data2) // convertimos el objeto a texto
            };
            // realizamos la petición AJAX usando fetch
            // el primer parámetro es el recurso del servidor al que queremos acceder
            // en este ejemplo, es un fichero php llamado media.php que se encuentra
            // dentro de la carpeta ./php y con el código PHP que hay arriba.
            // el segundo parámetro es el objeto init con la información sobre los
            // datos que queremos enviar, el método de envio, etc.
            var response = await fetch('http://localhost:8000/api/upload', init);
            if (response.ok) {
             console.log(response);
            } else {
                throw new Error(response.statusText);
            }
        } catch (err) {
            console.log("Error al realizar la petición AJAX: " + err.message);
        }
    })();

}
function changeColor(){
    var color = document.getElementById("colores");
    var simbols = document.getElementsByClassName("color");
    

    
    for (i = 0; i < simbols.length; i++) {
        simbols[i].style.fill = color.value;
      }
  
}
function colorContorno(){
    var color = document.getElementById("colores");
    var simbols = document.getElementsByClassName("color");
    

    
    for (i = 0; i < simbols.length; i++) {
        simbols[i].style.stroke = color.value;
      }
}
function fontSize(){
    var elemento =document.getElementById("panelEdicion");
   
    var valor = prompt("Ingrese el nuevo tamaño de letra en pixeles", "");
    elemento.style.fontSize=valor+"px";
}
function eliminarTodo(){
    document.getElementById('panelEdicion').innerHTML = '';
}
function agrandarXPanel(){
    var panel = document.getElementById("panelEdicion");
    var altura = panel.clientHeight;
    panel.style.height=altura+150+"px";
}
function encogerXPanel(){
    var panel = document.getElementById("panelEdicion");
    var altura = panel.clientHeight;
    panel.style.height=altura-150+"px";
}
function agrandarYPanel(){
    var panel = document.getElementById("panelEdicion");
    var altura = panel.clientWidth;
    panel.style.width=altura+150+"px";
}
function encogerYPanel(){
    var panel = document.getElementById("panelEdicion");
    var altura = panel.clientWidth;
    panel.style.width=altura-150+"px";
}
function eliminar(e) {
    var elementoArrastrado = document.getElementById(e.dataTransfer.getData("Data")); // Elemento arrastrado
    elementoArrastrado.parentNode.removeChild(elementoArrastrado); // Elimina el elemento
    e.target.style.border = '';   // Quita el borde
}

function leerArchivo(e) {
    var archivo = e.target.files[0];
    if (!archivo) {
      return;
    }
    var lector = new FileReader();
    lector.onload = function(e) {
      var contenido = e.target.result;
      mostrarContenido(contenido);
    };
    lector.readAsText(archivo);
  }
  
  function mostrarContenido(contenido) {
    var elemento = document.getElementById('pade');
    var json = JSON.parse(contenido);
   console.log(json.html);
   elemento.innerHTML = json.html;
  }
  
  //document.getElementById('file').addEventListener('change', leerArchivo, false);

