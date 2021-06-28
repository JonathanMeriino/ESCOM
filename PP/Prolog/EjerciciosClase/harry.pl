
hombre(james).
hombre(harry).
hombre(james_sirius).
hombre(albus).
hombre(arthur).
hombre(fred).
hombre(george).
hombre(ron).
hombre(hugo).


mujer(lily).
mujer(ginny).
mujer(luna).
mujer(molly).
mujer(hermione).
mujer(rose).


%matrimonio

matrimonio(james,lily).
matrimonio(harry,ginny).
matrimonio(molly,weasley).
matrimonio(ron,hermione).


%progenitura(hijo,padre). 

progenitura(harry,james).
progenitura(harry,lily).

progenitura(james_sirius,harry).
progenitura(albus,harry).
progenitura(luna,harry).

progenitura(james_sirius,ginny).
progenitura(albus,ginny).
progenitura(luna,ginny).

progenitura(rose,ron).
progenitura(hugo,ron).

progenitura(rose,hermione).
progenitura(hugo,hermione).

progenitura(ginny,arthur).
progenitura(fred,arthur).
progenitura(ron,arthur).
progenitura(george,arthur).

progenitura(ginny,molly).
progenitura(fred,molly).
progenitura(ron,molly).
progenitura(george,molly).

esposa(X,Y):-mujer(X),matrimonio(X,Y);matrimonio(Y,X).
hermanos(X,Y):-progenitura(X,Y),
                progenitura(X,Y),
                X\=Y.
tio(T,S):-progenitura(S,P),
            hermanos(P,T).

