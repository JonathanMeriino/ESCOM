let x=5; // declaración explicitas
var y=9;
/*alert(x);
alert(y)
alert (x+y);*/
for (var i=0;i<10;i++)
    x+=1;
alert ("Valor de × después del for"+x);
//suma(0);
//resta(15,10)
//resta(10);
//resta0;
//declaración implicita de una variable
resul=multi();
alert ("El resultado de la la multiplicación es: "+resul)

function suma(){
    let res=x+y;
    alert ("Suma:" +res) ;
}
function multi(){
    let res=x*y; 
    return(res); 
}
function resta(a,b){
    if(!b)
        b=3;
    if (!a)
        a=20;
    let res=a-b; 
    alert ("Resta:"+ res)
}


function factorial(dato){
    var resultadoFact = dato;
    for(var i = dato-1; i>= 1; i--){
        resultadoFact = resultadoFact *i;
    }
    alert("El factorial es: "+resultadoFact);
}

function potencia(base,exp){

    let resultado = Math.pow(base,exp);
    alert("La Potencia es: "+resultado);
}

function conversion(numero){
    switch(numero){
        case 1: console.log("Uno") 
            break;
        case 2: console.log("Dos") 
            break;
        case 3: console.log("Tres") 
            break;
        case 4: console.log("Cuatro") 
            break;
        case 5: console.log("Cinco") 
            break;
        case 6: console.log("Seis") 
            break; 
        case 7: console.log("Siete") 
            break;
        case 8: console.log("Ocho") 
            break; 
        case 9: console.log("Nueve") 
            break; 
        case 10: console.log("Diez") 
            break; 
        case 11: console.log("once") 
            break;
        case 12: console.log("doce") 
            break;
        case 13: console.log("trece") 
            break; 
        case 14: console.log("catorce") 
            break; 
        case 15: console.log("quince") 
            break;
        case 16: console.log("dieciseis") 
            break;
        case 17: console.log("diecisiete") 
            break; 
            
        case 61: console.log("sesenta y uno") 
            break;
        case 62: console.log("sesenta y Dos") 
            break;
        case 63: console.log("sesenta y Tres") 
            break;
        case 64: console.log("sesenta y Cuatro") 
            break;
        case 65: console.log("sesenta y Cinco") 
            break;
        case 66: console.log("sesenta y Seis") 
            break; 
        case 67: console.log("sesenta y Siete") 
            break;
        case 68: console.log("sesenta y cho") 
            break; 
        case 69: console.log("sesenta y Nueve") 
            break; 
        case 70: console.log("setenta") 
            break; 
        case 71: console.log("setenta y uno") 
            break;
        case 72: console.log("setenta y dos") 
            break;
        case 73: console.log("setenta y tres") 
            break; 
        case 74: console.log("setenta y cuatro") 
            break; 
        case 75: console.log("setenta y cinco") 
            break;
        case 76: console.log("setenta y seis") 
            break;
        case 77: console.log("setenta y siete") 
            break; 
    }
}

