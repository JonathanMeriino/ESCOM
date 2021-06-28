% Base de conocimiento, Coloque aquí los predicados para representar el
% conocimiento
plato_entrada(foie_gras,518).
plato_entrada(almejas,50).
plato_entrada(caviar,233).
plato_entrada(cabrito,127).
plato_entrada(faisan,144).

desayuno_plato(coctel_de_frutas,93).
desayuno_plato(quinoa_primavera,192).
desayuno_plato(pancake_avena,158).
desayuno_plato(sopa_col,83).
desayuno_plato(huevos_ahogados,171).

comida_plato(pechuga_pollo_mandarina,430).
comida_plato(croquetas_brocoli,529).
comida_plato(lasagna_berenjenas,292).
comida_plato(tlayuda,297).
comida_plato(sopa_tortilla,235).

cena_plato(tostada_tinga,249).
cena_plato(pozole,240).
cena_plato(pambazo,330).
cena_plato(sope_87).
cena_plato(quesadilla_293).

bebida(anis,312).
bebida(cafe,1).
bebida(cotatac,243).
bebida(pisco,210).
bebida(te,1).


% Ciclo principal

main:-repeat,
      pinta_menu,
      read(Opcion),
      ( (Opcion=1,doImc,fail);
	(Opcion=2,doDieta,fail);
	(Opcion=3,!)).

% Muestra el menú

pinta_menu:-nl,nl,
      writeln('===================================='),
      writeln('          DRA. TANIA ROSALES'),
      writeln('   <<  Experta en Nutrición  >>'),
      writeln('===================================='),
      nl,writeln('       MENU PRINCIPAL'),
      nl,write('1 Calcular indice de masa corporal'),
      nl,write('2 Recomendar una dieta saludable'),
      nl,write('3 Salir'),
      nl,write('================================='),
      nl,write('Indica tu opcion:').

% Regla para calcular IMC

doImc:-nl, write('================================='),nl,
       write('Elegiste: Calculo del Indice de Masa Corporal\n'),nl,
       write('Indique su peso en Kilogramos:'),read(Peso),
       write('Indique su estatura en Metros:'),read(Estatura),Estatura > 0,
       write('Indique su genero (1/Male, 2/Female):'),read(Sexo),
       IND is Peso/(Estatura*Estatura),
       nl,format('Su indice de masa corporal es: ~g',IND),
       nl, write('DIAGNOSTICO: '),
        (   (Sexo=1,IND<17,write('USTED PADECE DESNUTRICION!'));
	   (Sexo=1,IND>=17,IND<20,write('USTED TIENE BAJO PESO!\n'));
       (Sexo=1,IND>=20,IND<25,write('USTED TIENE PESO NORMAL!\n'));
        (Sexo=1,IND>=25,IND<30,write('USTED TIENE SOBREPESO!\n'));
        (Sexo=1,IND>=30,IND<35,write('USTED TIENE OBESIDAD!\n'));
        (Sexo=1,IND>=35,IND<40,write('USTED TIENE OBESIDAD MARCADA!\n'));
        (Sexo=1,IND>40,write('USTED TIENE OBESIDAD MORBIDA!\n'));

       (Sexo=2,IND<16,write('USTED PADECE DESNUTRICION!'));
	   (Sexo=2,IND>=16,IND<20,write('USTED TIENE BAJO PESO!\n'));
       (Sexo=2,IND>=20,IND<24,write('USTED TIENE PESO NORMAL!\n'));
        (Sexo=2,IND>=24,IND<29,write('USTED TIENE SOBREPESO!\n'));
        (Sexo=2,IND>=29,IND<34,write('USTED TIENE OBESIDAD!\n'));
        (Sexo=2,IND>=34,IND<39,write('USTED TIENE OBESIDAD MARCADA!\n'));
        (Sexo=2,IND>40,write('USTED TIENE OBESIDAD MORBIDA!\n')) ).

% Regla para recomendar dietas

doDieta:-nl,writeln('Elegiste: Nutriologo Artificial'),

    write('Ingrese su edad: '), read(Edad),
    write('Indique su peso en kilogramos: '), read(Peso),
    write('Indique su genero (1/Male, 2/Female'), read(Sexo),
        (  (Sexo=1, Edad<25,Cal is (Peso*24)+300);
           (Sexo=1, Edad>=25,Edad=<45,Cal is Peso*24);
           (Sexo=1, Edad>45,Edad=<55,Cal is (Peso*24)-100);
           (Sexo=1, Edad>55,Edad=<65,Cal is (Peso*24)-200);
           (Sexo=1, Edad>65,Edad=<75,Cal is (Peso*24)-300);
           (Sexo=1, Edad>75,Edad=<85,Cal is (Peso*24)-400);
           (Sexo=1, Edad>85,Edad=<95,Cal is (Peso*24)-500);
           (Sexo=1, Edad>95,Edad=<105,Cal is (Peso*24)-600);


           (Sexo=2, Edad<25,Cal is (Peso*21.6)+300);
           (Sexo=2, Edad>=25,Edad=<45,Cal is Peso*21.6);
           (Sexo=2, Edad>45,Edad=<55,Cal is (Peso*21.6)-100);
           (Sexo=2, Edad>55,Edad=<65,Cal is (Peso*21.6)-200);
           (Sexo=2, Edad>65,Edad=<75,Cal is (Peso*21.6)-300);
           (Sexo=2, Edad>75,Edad=<85,Cal is (Peso*21.6)-400);
           (Sexo=2, Edad>85,Edad=<95,Cal is (Peso*21.6)-500);
           (Sexo=2, Edad>95,Edad=<105,Cal is (Peso*21.6)-600) ),

    nl, format('Las calorias que puedes consumir al dia son: ~g ',[Cal]),
    
    desayuno_plato(platoDesayu,K_platoDesayu),bebida(Bebida,K_Bebida),
    Total_des is K_platoDesayu + K_Bebida,

    plato_entrada(Entrada,K_Entrada),comida_plato(platoComida,K_platoComida),bebida(Bebida,K_Bebida),
    Total_comida is K_Entrada + K_platoComida + K_Bebida,

    cena_plato(platoCena,K_platoCena),bebida(Bebida,K_Bebida),
    Total_cena is K_platoCena + K_Bebida,

    Total is  Total_des + Total_comida + Total_cena,
    Total >= Cal*0.9,Total =< Cal*1.1,

    nl, format('De desayuno ~s con ~s es saludable, la suma de calorías es ~g',[platoDesayu, Bebida, Total_des]),

    nl, format('De comida ~s con ~s y ~s es saludable, la suma de calorías es ~g',[platoComida, Bebida, Total_comida]),

    nl, format('De cena ~s con ~s es saludable, la suma de calorías es ~g',[platoCena, Bebida, Total_cena]),

    nl, format('TOTAL DE CALORIAS CONSUMIDAS EN EL DIA ~g\n<<Press Enter>>\n',[Total]),

    get_single_char(_), fail.

cls:-write('[\e[2J').


