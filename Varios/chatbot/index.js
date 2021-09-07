const products = [
    {producto: 'Arroz' ,mercado: 'Walmart', precio: 15},
    {producto: 'Arroz' ,mercado: 'Superama', precio: 25},
    {producto: 'Arroz' ,mercado: 'Bodega aurrera', precio: 20},
    {producto: 'Arroz' ,mercado: 'Tienda Don Pancho', precio: 13},
    {producto: 'Arroz' ,mercado: 'Waldos', precio: 30},
];




const productsFilter = products.filter(x => x.precio < 20)

console.log(productsFilter)