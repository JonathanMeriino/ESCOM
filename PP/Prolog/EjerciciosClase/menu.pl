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
      nl,write('1 Calcular indice de masa corporal'),
      nl,write('2 Recomendar una dieta saludable'),
      nl,write('3 Salir'),
      nl,write('================================='),
      nl,write('Indica tu opcion:').

doOpcion1:-writeln('Elegiste la opción 1').
doOpcion2:-writeln('Elegiste la opción 2').
doOpcionSalir:-writeln('Vuelve Pronto').
