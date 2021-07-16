main:-repeat,
      pinta_menu,
      read(Opcion),
      ( (Opcion=1,doOpcion1,fail);
	(Opcion=2,doOpcion2,fail);
	(Opcion=3,doOpcionSalir,!)).

% Muestra el menú

pinta_menu:-nl,nl,
      writeln('===================================='),
      nl,writeln('       MENU PRINCIPAL'),
      nl,write('1 Convertir de Dolares a Pesos'),
      nl,write('2 Convertir de Pesos a dolares'),
      nl,write('3 Salir'),
      nl,write('================================='),
      nl,write('Indica tu opcion:').

doOpcion1:-writeln('Elegiste la opción 1'),
            writeln(' Dame el valor que quieras convertir '), read(A),
            C is A*1/20.38,
            format('La conversion en dolar es: ~g',C).
doOpcion2:-writeln('Elegiste la opción 2'),
            writeln(' Dame el valor que quieras convertir '), read(A),
            C is A*20.38/1,
            format('La conversion en pesos es: ~g',C).
doOpcionSalir:-writeln('Vuelve Pronto').
