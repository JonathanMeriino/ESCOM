function getBotResponse(input) {
    //
    if (input == "papers") {
        return "rocks";
    } else if (input == "rocks") {
        return "papers";
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
        return "Trata preguntando otra cosa!";
    }
}



