%Autor:
%Fecha:
%Introducción a Prolog

%Hechos

humano(socrates).
humano(platon).
humano(aristoteles).

% discipulo(discipulo, maestro).

discipulo(socrates,platon).
discipulo(platon,aristoteles).

%Reglas

es_mortal(X):-humano(X).

%Consultar   ?- es_mortal(socrates).
