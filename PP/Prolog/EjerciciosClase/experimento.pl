% Base de conocimiento, Coloque aquí los predicados para representar el
% conocimiento



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

doDieta:-nl,write('Elegiste: Nutriologo Artificial'),nl,
    write('Indique su edad :'),read(Edad),
    write('Indique su peso en kg:'),read(Peso),
    write('Indique su genero (1/Male, 2/Femele):'),read(Sexo),
    MET_M is Peso*24,
    MET_H is Peso*21.6,
    A is MET_M + 300,
    B is MET_H+300,
    ((Sexo=1,Edad<25,nl,format('Las calorias que debe comer al d�a es : ~g',A));
    (sexo=2,Edad<25,nl,format('Las calorias que debe comer al dia es :  ~g',B));
    (sexo=1,edad>=25,edad<45,format('Las calorias que debe comer al es :~g',MET_M));
    (sexo=2,edad>=25,edad<45,format('Las calorias que debe comer al es :~
g',MET_H))).
