



const productsArroz = [
    {producto: 'Arroz' ,place: 'CDMX', precio: 14},
    {producto: 'Arroz' ,place: 'SanLuis', precio: 18},
    {producto: 'Arroz' ,place: 'Campeche', precio: 21},
    {producto: 'Arroz' ,place: 'Yucatan', precio: 33},
    {producto: 'Arroz' ,place: 'edoMex', precio: 3},
];


const productsMantequilla = [
    {producto: 'Mantequilla' ,lugar: 'Walmart', precio: 15},
    {producto: 'Mantequilla' ,lugar: 'Superama', precio: 25},
    {producto: 'Mantequilla' ,lugar: 'Bodega aurrera', precio: 20},
    {producto: 'Mantequilla' ,lugar: 'Tienda Don Pancho', precio: 13},
    {producto: 'Mantequilla' ,lugar: 'Waldos', precio: 30},
];

function buscoMantequilla() {
    
    const wantMantequilla = productsMantequilla.filter(x => x.producto == 'Mantequilla' & x.precio <20 & x.lugar == 'Walmart')

    return console.log(wantMantequilla);
}

buscoMantequilla();

function buscoArroz(){

    const wantArroz = productsArroz.filter(x => x.producto == 'Arroz' & x.precio < 15 & x.place == 'CDMX')
    
    return console.log(wantArroz);

}

buscoArroz();


