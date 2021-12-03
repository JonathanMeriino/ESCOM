%Problema1 

disco(easy,(interprete(commondors),genero(rock),año(1955))).

disco(melody,(interprete(bee_gees),genero(balada),año(1979))).
disco(weakness,(interprete(joan_armatrading),genero(blues),año(1970))).

disco(halo,(interprete(beyonce),genero(poop),año(2005))).

disco(love_me,(interprete(the_beatles),genero(rock),año(1967))).
disco(help,(interprete(the_beatles),genero(rock),año(1965))).

disco(words,(interprete(f_david),genero(poop),año(1983))).
disco(kashmir,(interprete(led_zeppelin),genero(rock),año(1970))).
disco(cloud9,(interprete(beach_bunny),genero(indie),año(2015))).
disco(black_dog,(interprete(led_zeppelin),genero(rock),año(1975))).

%Problema2

empresa(departamento(development),empleado(nombre(leo_merino),cargo(software_analyst),salario(2000))).
empresa(departamento(development),empleado(nombre(gio_merino),cargo(desarrollador),salario(2500))).
empresa(departamento(publicidad),empleado(nombre(pau_garcia),cargo(marketing),salario(2000))).
empresa(departamento(diseño),empleado(nombre(carlos_gomez),cargo(diseñador),salario(1500))).
empresa(departamento(recursos_humanos),empleado(nombre(itati_aragon),cargo(recruitment),salario(3000))).

%Problema3

lenguaje(c).
lenguaje(python).
lenguaje(perl).

deriva(python,c).
deriva(perl,c).

lenguajes(php,paradigma(multiparadigma),sistema(multiplataforma)).
lenguajes(java,paradigma(objetos),sistema(multiplataforma)).
lenguajes(basic,paradigma(imperativo),sistema(multiples)).
tipo(python, nivel(alto_nivel),lenguaje(familiar)).
tipo(php,nivel(alto_nivel),lenguaje(familiar)).
tipo(ensamblador,nivel(bajo_nivel),lenguaje(codigos)).
tipo(maquina, nivel(binario),lenguaje(maquina)).


espadre(X,Y):-deriva(Y,X).

