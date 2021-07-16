frame(animal,subclase_de(objeto),propiedades([puede(sentir), puede(respirar)])).
frame(insecto,subclase_de(animal), propiedades([tiene(exoesqueleto)])).
frame(reptil,subclase_de(animal), propiedades([tiene(escamas),tiene(sangre_fria)])).
frame(luciernaga,subclase_de(insecto), propiedades([tiene(trasero_luminoso)])).
frame(caiman,subclase_de(reptil), propiedades([tiene(hocico_grande)])).
frame(ray,instancia_de(luciernaga), propiedades([])).
frame(louis,instancia_de(caiman), propiedades([gusta(jazz)])).


que_es(X):-((instancia(X),es(Clase,X));
	    (subclase(X),subc(X,Clase))),Clase\=objeto,write('es '),writeln(Clase),fail.
es(Clase,Obj):- frame(Obj,instancia_de(Clase),_).
es(Clase,Obj):- frame(Obj,instancia_de(Clasep),_),subc(Clasep,Clase).

subc(C1,C2):- frame(C1,subclase_de(C2),_).
subc(C1,C2):- frame(C1,subclase_de(C3),_),subc(C3,C2).

subclase(X):-frame(X,subclase_de(_),_).
instancia(X):-frame(X,instancia_de(_),_).

propiedadesc(objeto):-!.
propiedadesc(X):-frame(X,subclase_de(Y),propiedades(Z)),imprime(Z),propiedadesc(Y).
propiedadesi(X):-frame(X,instancia_de(Y),propiedades(Z)),imprime(Z),propiedadesc(Y).

props(X):-(instancia(X),propiedadesi(X));(subclase(X),propiedadesc(X)).

imprime([]):-!.
imprime([H|T]):-writeln(H),imprime(T).

que_puedes_decirme_de(X):-que_es(X);props(X).



















