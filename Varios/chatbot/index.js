const productsArroz = [
    {place: 'CDMX', precio: 14},
    {place: 'SanLuis', precio: 18},
    {place: 'Campeche', precio: 21},
    {place: 'Yucatan', precio: 33},
    {place: 'edoMex', precio: 3},
];
const productsMantequilla = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsLeche = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsFrijol = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsHuevo = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsTortilla = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsFrutas = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsVerduras = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsAceite = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];
const productsAzucar = [
    {lugar: 'Walmart', precio: 15},
    {lugar: 'Superama', precio: 25},
    {lugar: 'Bodega aurrera', precio: 20},
    {lugar: 'Tienda Don Pancho', precio: 13},
    {lugar: 'Waldos', precio: 30},
];

function buscoMantequilla() {
    
    const wantMantequilla = productsMantequilla.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantMantequilla);
} 

function buscoArroz(){

    const wantArroz = productsArroz.filter(x => x.precio < 15 & x.place == 'CDMX')
    
    return console.log(wantArroz);
} 
function buscoLeche(){

    const wantLeche = productsLeche.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantLeche);
}
function buscoFrijol(){

    const wantFrijol = productsFrijol.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantFrijol);
}
function buscoHuevo(){

    const wantHuevo = productsHuevo.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantHuevo);
}
function buscoTortilla(){

    const wantTortilla = productsTortilla.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantTortilla);
}
function buscoFruta(){

    const wantFruta = productsFruta.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantFruta);
}
function buscoVerdura(){

    const wantVerdura = productsVerduras.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantVerdura);
}
function buscoAzucar(){

    const wantAzucar = productsAzucar.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantAzucar);
}
function buscoAceite(){

    const wantAceite = productsAceite.filter(x => x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantAceite);
}

if (input == "busco mantequilla") {
    return buscoMantequilla();
} else if (input == "busco arroz") {
    return buscoArroz();
} else if (input == "busco huevo") {
    return buscoHuevo();
} else if (input == "busco leche"){
    return buscoLeche();
}else if (input == "busco Tortilla"){
    return buscoTortilla();
}else if (input == "busco frijol"){
    return buscoFrijol();
}else if (input == "busco frutas"){
    return buscoFruta();
}else if (input == "busco verduras"){
    return buscoVerduras();
}else if (input == "busco aceite"){
    return buscoAceite();
}else if (input == "busco azucar"){
    return buscoAzucar();
}
