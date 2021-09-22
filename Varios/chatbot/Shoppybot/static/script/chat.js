// Collapsible
//retorna un objeto similar a un array que tenga todos los nombres de la clase indicados
var coll = document.getElementsByClassName("collapsible");
// declaracion de variables
let start=0;
let lasagna = ["cebolla","ajo","aceite de oliva", "carne molida", "zanahoria", "apio", "sal", "pimienta", "albahaca seca", "salsa de jitomate", "pasta para lasagna", "crema", "queso manchego", "queso parmesano"];
let spaghetti = ["spaguetti", "aceite de oliva", "ajo", "cebolla", "zanahoria", "carne molida", "caldo de carne", "tomate", "azucar", "perejil fresco", "sal", "pimienta", "queso parmesano"];
let masaPizza=["levadura", "sal", "aceite de oliva", "harina"];
let chilesNogada=["chiles poblanos","granadas rojas", "perejil", "cebolla", "ajo", "carne molida", "acitron", "pasas", "almendra", "durazno", "pera", "manzana", "azucar", "canela","sal","pimienta","manteca","nuez castilla","queso crema","vino blanco","nueces moscada","leche de vaca"];
let productos=["cebolla","ajo","aceite de oliva","carne molida","zanahoria", "apio", "sal", "pimienta", "albahaca seca", "salsa de jitomate", "pasta para lasagna", "crema", "queso manchego", "queso parmesano"
,"spaguetti", "tomate", "azucar", "perejil fresco", "levadura", "harina","chiles poblanos", "granadas rojas", "acitron", "pasas", "almendra", "durazno","pera","manzana","canela", "manteca","nuez castilla", "queso crema", "vino blanco", "nueces moscada", "leche de vaca"];
var j=0;
let lugares=["Walmart", "Soriana", "Chedrui", "Aurrera", "Costco"];
let walmartPrecio=[15,60,20,90,25,15,20,20,15,80,75,90,90,23,50,45,20,40,80,40,50,60,60,60,55,60,45,30,90,50,60,85,65,22,20];
let sorianaPrecio;
let chedrauiPrecio;
let aurreraPrecio;
let precioCostco;


for (let i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () { //registra un evento a un objeto en especifico
        this.classList.toggle("active");     //accede a la lista de clases de un elemento   

        var content = this.nextElementSibling;  // devuelve el elemento posterior al especificado

        if (content.style.maxHeight) { 
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }

    });
}
//funcion que optiene el tiempo
function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// funcion para el primer mensaje del bot
function firstBotMessage() {
    let firstMessage = "Bienvenido, mi nombre es Shopy. ¿En qué puedo ayudarte?"
    //devuelve una referencia al elemento por su ID
    document.getElementById("botStarterMessage").innerHTML = '<p class="botText"><span>' + firstMessage + '</span></p>';
    
    let time = getTime();

    $("#chat-timestamp").append(time);
    document.getElementById("userInput").scrollIntoView(false);



    botResponse= "Te puedo ayudar a encontrar productos en los lugares donde los venden, posibles precios y en caso de que desees preparar algún platillo te puedo sugerir los ingredientes";
    botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
  
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    botResponse= "¿Deseas comenzar?";
    botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
  
    $("#chatbox").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

firstBotMessage();

//base de conocimiento
function getHardResponse(userText) {

    if(userText=="Comenzar"||userText=="New"||start==1||userText=="comenzar"||userText=="sí"||userText=="Sí"){
        if (j==0){
            start=1;
            botResponse = "Dime que producto buscas o el platillo que quieres cocinar:";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
            $("#chatbox").append(botHtml);
            document.getElementById("chat-bar-bottom").scrollIntoView(true);
            j=j+1;
        }
        if (userText==="Cancelar"||userText==="cancelar"||userText==="no"||userText==="No"){
            botResponse = "Busqueda Cancelada, ¡Hasta luego!";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
            $("#chatbox").append(botHtml);
            document.getElementById("chat-bar-bottom").scrollIntoView(true);
            star=0;
            j=0;
            producto=0;
            i=0;
            loops=0;
            return;
        }
        if (userText=="chiles en Nogada"||userText=="chiles nogada"){
            botResponse= "Los ingredientes que necesitas son:";
                    botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
  
                    $("#chatbox").append(botHtml);

                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
            for (i=0;i<chilesNogada.length;i++){
                    botResponse= chilesNogada[i];
                    botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
  
                    $("#chatbox").append(botHtml);

                    document.getElementById("chat-bar-bottom").scrollIntoView(true);
            }
            botResponse= "¿Deseas saber donde puedes comprar algún producto?";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }
        else if (userText=="spaghetti a la bolonesa"||userText=="Espagueti a la bolonesa"|| userText=="Spaguetti a la bolonesa"||userText=="espagueti a la bolonesa"){
            botResponse= "Los ingredientes que necesitas son:";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
            for (i=0;i<spaghetti.length;i++){
                botResponse= spaghetti[i];
                botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

                $("#chatbox").append(botHtml);

                document.getElementById("chat-bar-bottom").scrollIntoView(true);
            }
            botResponse= "¿Deseas saber donde puedes comprar algún producto?";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }
        else if(userText=="masa para pizza"||userText=="Masa para pizza"){
            botResponse= "Los ingredientes que necesitas son:";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
            for (i=0;i<masaPizza.length;i++){
                botResponse= masaPizza[i];
                botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

                $("#chatbox").append(botHtml);

                document.getElementById("chat-bar-bottom").scrollIntoView(true);
            }
            botResponse= "¿Deseas saber donde puedes comprar algún producto?";
                botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

                $("#chatbox").append(botHtml);

                document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }
        else if(userText=="lasagna"||userText=="Lasagna"||userText=="lasaña"||userText=="Lasaña"){
            botResponse= "Los ingredientes que necesitas son:";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
            for (i=0;i<lasagna.length;i++){
                    
                botResponse= lasagna[i];
                botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

                $("#chatbox").append(botHtml);

                document.getElementById("chat-bar-bottom").scrollIntoView(true);
                }
            
            botResponse= "¿Deseas saber donde puedes comprar algún producto?";
                botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

                $("#chatbox").append(botHtml);

                document.getElementById("chat-bar-bottom").scrollIntoView(true);
                
                
        }
        else if(userText=="sí"||userText=="si"||userText=="Sí"||userText=="Si"){
            botResponse= "¿Qué producto deseas conocer?";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }
        else if(userText=="producto"){
            botResponse= "¿Qué producto deseas conocer?";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';

            $("#chatbox").append(botHtml);

            document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }
        else if(userText =="Cebolla"||userText =="cebolla"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "Lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="ajo"||userText =="Ajo"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="aceite de oliva"||userText =="Aceite de oliva"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="carne molida"||userText =="Carne molida"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="zanahoria"||userText =="Zanahoria"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="apio"||userText =="Apio"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }else if(userText =="sal"||userText =="Sal"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="pimienta"||userText =="Pimienta"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="albahaca seca"||userText =="Albahaca seca"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="salsa de jitomate"||userText =="Salsa de jitomate"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="pasta para lasagna"||userText =="Pasta para lasagna"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }       
        else if(userText =="crema"||userText =="Crema"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="queso manchego"||userText =="Queso manchego"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="queso parmesano"||userText =="Queso parmesano"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="spaguetti"||userText =="Spaguetti"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="tomate"||userText =="Tomate"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="azucar"||userText =="Azucar"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="perejil fresco"||userText =="Perejil fresco"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="levadura"||userText =="Levadura"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="harina"||userText =="Harina"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="chiles poblanos"||userText =="Chiles poblanos"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="granadas rojas"||userText =="Granadas rojas"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="acitron"||userText =="Acitron"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="pasas"||userText =="Pasas"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="almendra"||userText =="Almendra"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="durazno"||userText =="Durazno"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="pera"||userText =="Pera"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="manzana"||userText =="Manzana"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="canela"||userText =="Canela"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }else if(userText =="manteca"||userText =="Manteca"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="nuez moscada"||userText =="Nuez moscada"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="Nuez castilla"||userText =="nuez castilla"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="queso crema"||userText =="Queso crema"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="vino blanco"||userText =="Vino blanco"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }
        else if(userText =="leche de vaca"||userText =="Leche de vaca"){
            for(i=0;i<productos.length;i++){
                if(userText==productos[i]){
                    for(k=0;k<lugares.length;k++){
                        botResp= lugares[k];
                        if(k==0)
                        botRespo= walmartPrecio[i];
                        else if(k==1)
                        botRespo=walmartPrecio[i]*.99;
                        else if(k==2)
                        botRespo=walmartPrecio[i]*1.02;
                        else if(k==3)
                        botRespo=walmartPrecio[i]*1.1;
                        else
                        botRespo=walmartPrecio[i]*1.8;
                        botResponse= "lo puedes encontrar en: "+ botResp+ " a un precio de: $"+botRespo
                        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        
                        $("#chatbox").append(botHtml);
        
                        document.getElementById("chat-bar-bottom").scrollIntoView(true);
                    }
                }
            }
        }

        else if (userText!="Comenzar"&&userText!="New"&&userText!="Sí"&&userText!="No"&&userText!="Cancelar"&&userText!="comenzar"&&userText!="cebolla"&&userText!="Cebolla"&&userText!="ajo"&&userText!="Ajo"&&userText!="aceite de oliva"
        &&userText!="Aceite de oliva"&&userText!="carne molida"&&userText!="Carne molida"&&userText!="zanahoria"&&userText!="Zanahoria"&&userText!="apio"&&userText!="Apio"&&userText!="sal"&&userText!="Sal"&&userText!="pimienta"&&userText!="Pimienta"
        &&userText!="albahaca seca"&&userText!="Albahaca seca"&&userText!="Salsa de jitomate"&&userText!="salsa de jitomate"&&userText!="pasta para lasagna"&&userText!="Pasta para lasagna"&&userText!="crema"&&userText!="Crema"&&userText!="queso manchego"&&userText!="Queso manchego"
        &&userText!="queso parmesano"&&userText!="Queso parmesano"&&userText!="spaguetti"&&userText!="Spaguetti"&&userText!="tomate"&&userText!="Tomate"&&userText!="azucar"&&userText!="Azucar"&&userText!="perejil fresco"&&userText!="Perejil fresco"
        &&userText!="levadura"&&userText!="Levadura"&&userText!="harina"&&userText!="Harina"&&userText!="chiles poblanos"&&userText!="Chiles poblanos"&&userText!="granadas rojas"&&userText!="Granadas rojas"&&userText!="acitron"&&userText!="Acitron"&&userText!="pasas"&&userText!="Pasas"
        &&userText!="almendra"&&userText!="Almendra"&&userText!="durazno"&&userText!="Durazno"&&userText!="durazno"&&userText!="pera"&&userText!="Pera"&&userText!="manzana"&&userText!="Manzana"&&userText!="canela"&&userText!="Canela"&&userText!="manteca"&&userText!="Manteca"&&userText!="nuez castilla"
        &&userText!="Nuez castilla"&&userText!="queso crema"&&userText!="Queso crema"&&userText!="vino blanco"&&userText!="Vino blanco"&&userText!="nuez moscada"&&userText!="Nuez moscada"&&userText!="leche de vaca"&&userText!="Leche de vaca"&&userText!="no"&&userText!="cancelar"){
            botResponse = "Lo siento, no entiendo a lo que te refieres, aún me encuentro aprendiendo para poder ser mejor. Escribe cancelar, si deseas cancelar la busqueda.";
            botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
            $("#chatbox").append(botHtml);
            document.getElementById("chat-bar-bottom").scrollIntoView(true);
        }

    }
    else if(userText==="Cancelar"||userText==="cancelar"||userText==="no"||userText==="No"){
        botResponse = "¡Hasta luego!";
        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        $("#chatbox").append(botHtml);
        document.getElementById("chat-bar-bottom").scrollIntoView(true);

    }
    else{
        botResponse = "Lo siento, no entiendo a lo que te refieres, aún me encuentro aprendiendo para poder ser mejor. Escribe cancelar, si deseas cancelar la busqueda.";
        $("#chatbox").append(botHtml);
        botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
        document.getElementById("chat-bar-bottom").scrollIntoView(true);
    }
}

   // let botResponse = getBotResponse(userText);
    //let botHtml = '<p class="botText"><span>' + botResponse + '</span></p>';
   // $("#chatbox").append(botHtml);

   // document.getElementById("chat-bar-bottom").scrollIntoView(true);


//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textInput").val();

    if (userText == "") {
        userText = " ";
    }

    let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 1000)

}

// Handles sending text via button clicks
function buttonSendText(sampleText) {
    let userHtml = '<p class="userText"><span>' + sampleText + '</span></p>';

    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    //Uncomment this if you want the bot to respond to this buttonSendText event
    // setTimeout(() => {
    //     getHardResponse(sampleText);
    // }, 1000)
}

function sendButton() {
    getResponse();
}

function heartButton() {
    buttonSendText("Heart clicked!")
}

// Press enter to send a message
$("#textInput").keypress(function (e) {
    if (e.which == 13) {
        getResponse();
    }
});