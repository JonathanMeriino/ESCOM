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


function getBotResponse(input) {
    //rock paper scissors
    if (input == "menor a 20") {
        const productsFilter = products.filter(x => x.precio < 20)
        return console.log(productsFilter);
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Respuestas de bienvenida y despedida
    if (input == "hola") {
        return "Hola, en que puedo ayudarte?";
    }else if (input == "Hola") {
        return "Bienvenido, en que puedo ayudarte";

    }else if (input == "bye") {
        return "Vuelve pronto!";
    } else if (input == "bye"){
        return "Adios, gracias por visitarnos";

    } else {
        return "Try asking something else!";
    }
}

