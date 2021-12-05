espadre(pablo,marcela).
espadre(pablo,juan).

espadre(juan,maria).

eshijo(X,Y):- espadre(Y,X).
esabuelo(X,Y):- espadre(X,Z),eshijo(Z,Y).

hermanos(X,Y):-espadre(Z,Y),
                espadre(Z,Y),
                X\=Y.
familiarde(X,Y):- espadre(X,Y).
familiarde(X,Y):- eshijo(X,Y).
familiarde(X,Y):- hermanos(X,Y).

% hechos

empleado(john_doe,trabajo(analista_software),salario(2000)).
