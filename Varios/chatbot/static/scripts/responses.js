
const products = [
    {producto: 'Arroz' ,mercado: 'Walmart', precio: 15},
    {producto: 'Arroz' ,mercado: 'Superama', precio: 25},
    {producto: 'Arroz' ,mercado: 'Bodega aurrera', precio: 20},
    {producto: 'Arroz' ,mercado: 'Tienda Don Pancho', precio: 13},
    {producto: 'Arroz' ,mercado: 'Waldos', precio: 30},
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

function recomendacion(input){

    if(input == "recomendacion de hoy"){
        return getBestProduct();
        
    }

}
function getBestProduct(){
        resultado = 2 + 5;
}