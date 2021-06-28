
hombre(homero).
hombre(abraham).
hombre(clancy).
hombre(bart).
hombre(mr_burns).
hombre(seymour_skinner).
hombre(milhouse).

mujer(marge).
mujer(lisa).
mujer(maggie).
mujer(mona).
mujer(jacqueline).
mujer(paty).
mujer(selma).
mujer(edna_krabappel).

mascota(ayudante_santa).
mascota(snowball).

alien(kang).


%matrimonio

matrimonio(homero,marge).
matrimonio(abraham,mona).
matrimonio(clancy,jacqueline).
matrimonio(kang,marge).

%progenitura(padre,hijo). 

padre(abraham,homero).
madre(mona,homero).

padre(clancy,marge).
madre(jacqueline,marge).

padre(clancy,selma).
madre(jacqueline,selma).

padre(clancy,paty).
madre(jacqueline,paty).

padre(homero,bart).
padre(homero,lisa).

madre(marge,bart).
madre(marge,lisa).

padre(kang,maggie).
madre(marge,maggie).


esposa(Y):-mujer(Y),matrimonio(X,Y).
esposo(X):-hombre(X),matrimonio(X,Y).

abuelo(X,Y):-hombre(X), padre(X,Z), padre(Z,Y).
abuelo(X,Y):-hombre(X), padre(X,Z), madre(Z,Y).

abuela(X,Y):-mujer(X), madre(X,Z), padre(Z,Y).
abuela(X,Y):-mujer(X), madre(X,Z), madre(Z,Y).

hermano(X,Y):- padre(Z,X),padre(Z,Y),
                madre(W,X),madre(W,Y),
                X\=Y.

cunado(X,Y):- hombre(X), matrimonio(X,Z), hermano(Z,Y). 

cunada(X,Y):- mujer(X), matrimonio(X,Z), hermano(Z,Y).


