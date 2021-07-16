propiedad(animal,puede,sentir).
propiedad(animal,puede,mover).
propiedad(animal,puede,respirar).
propiedad(ave,puede,volar).
propiedad(mamifero,puede,mamar).
propiedad(gallo,puede,cantar).
propiedad(ave,tiene,plumas).
propiedad(raton,puede,correr).
propiedad(gato,come,raton).
propiedad(halcon,come,gallo).

subclase(animal,top).
subclase(ave,animal).
subclase(mamifero,animal).
subclase(gallo,ave).
subclase(halcon,ave).
subclase(gato,mamifero).
subclase(raton,mamifero).

instancia(foghorn_leghorn,gallo).
instancia(henery_hawk,halcon).
instancia(silvester_jr,gato).
instancia(speedy_gonzales,raton).

que_es(X):-((instancia(X),es(Clase,X));
	    (subclase(X),subc(X,Clase))),
	    Clase\=top,write('es '),writeln(Clase),fail.

es(Clase,Obj):- instancia(Obj,Clase).
es(Clase,Obj):- instancia(Obj,Clasep),subc(Clasep,Clase).

subc(C1,C2):- subclase(C1,C2).
subc(C1,C2):- subclase(C1,C3),subc(C3,C2).

instancia(X):-instancia(X,_).
subclase(X):-subclase(X,_).

propias(X):-propiedad(X,Y,Z),write(Y),write(' '), write(Z), writeln(''), fail.

prop_sub(X):- not(propias(X)),subclase(X,Y), prop_sub(Y).

prop_ins(X):-instancia(X,Y), prop_sub(Y).

propiedades(X):-prop_sub(X);prop_ins(X).

que_puedes_decirme_de(X):-que_es(X);propiedades(X).
















