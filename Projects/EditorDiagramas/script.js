
function inicio() {
    var panel = document.getElementById("panelEdicion");
 panel.innerHTML="<svg width='300px' height='300px'><rect x='60' y='10' rx='200' ry='120' width='200px' height='120px'style=' fill: white; stroke:black; stroke-width: 2px;' /></svg>"
}

function declaracionVariables() {
    var panel = document.getElementById("panelEdicion");
 panel.innerHTML="<svg width='300px' height='300px'><rect x='60' y='10' rx='15' ry='15' width='200px' height='20px'style=' fill: white; stroke:black; stroke-width: 2px;' /><rect x='60' y='30' rx='10' ry='10' width='200px' height='100px'style=' fill: white; stroke:black; stroke-width: 2px;' /><rect x='60' y='130' rx='15' ry='15' width='200px' height='20px'style=' fill: white; stroke:black; stroke-width: 2px;' /></svg>"
     
}

function entradaDatos() {
    var panel = document.getElementById("panelEdicion");
    panel.innerHTML="<svg width=310 height=310> <path d='M 10 270 Q 75 200 150 270 T 300 270  M 300 280 z'stroke='navy' stroke-width=2 fill='white' /><line x1='10' y1='10' x2='10' y2='270' style='stroke:navy;stroke-width:2'/><line x1='10' y1='10' x2='300' y2='10' style='stroke:navy;stroke-width:2'/><line x1='300' y1='10' x2='300' y2='270' style='stroke:navy;stroke-width:2'/></svg>"


}
function salidaDatos(){
    var panel = document.getElementById("panelEdicion");
    panel.innerHTML="<svg width=200 height=150><polygon points='10,140 10,50 40,10 190,10 190,140 ' style='fill:white;stroke:navy;stroke-width:2' /></svg>"
    
}
function sentenciaSimple(){
    var panel = document.getElementById("panelEdicion");
    panel.innerHTML="<svg width='300px' height='300px'><rect x='60' y='10' width='200px' height='120px'style=' fill: white; stroke:black; stroke-width: 2px;' /></svg>"

}
function condicional(){
    var panel = document.getElementById("panelEdicion");
    panel.innerHTML=" <p>if</p><svg width='150px' height='150px'><polygon points='0,75 75,0 150,75 75,150' style='fill:white;stroke:navy;stroke-width:2' /></svg>"
}
function repeticion(){
   
    var panel = document.getElementById("panelEdicion");
    panel.innerHTML="<p>For</p> <svg width='150px' height='150px'><polygon points='0,75 75,0 150,75 75,150' style='fill:white;stroke:navy;stroke-width:2' /></svg>"
}
function end(){
    var panel = document.getElementById("panelEdicion");
 panel.innerHTML="<svg width='300px' height='300px'><rect x='60' y='10' rx='200' ry='120' width='200px' height='120px'style=' fill: white; stroke:red; stroke-width: 2px;' /></svg>"

}

function save(){
    alert("save");

}
function upload(){
    alert("upload");
}
function changeColor(){
    alert("changeColor");
}
function colorContorno(){
    alert("Color contorno");
}
function fontSize(){
    alert("fontSize");
}
function eliminar(){
    alert("eliminar");
}



