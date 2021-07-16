:- dynamic si/1,no/1.

/**************************************************
Implementacion de un pequeño sistema experto
***************************************************/

% Motor de inferencia

satisface(Atributo,_) :-
   (si(Atributo)  -> true ;                %if   si(Atributo) then true
    (no(Atributo) -> fail ;		   %else if no(Atributo) then fail
                     pregunta(Atributo))). %else pregunta(Atributo)

pregunta(A) :-
    write('¿El objeto '),
    write(A), write('?'),
    read(Resp),
    nl,
    ((Resp = s ; Resp = si)                 %if Resp = s or Resp = si then
      -> assert(si(A));                     %     assert(si(A))
         assert(no(A)), fail).		    %else assert(no(A))

explica:-writeln('\nLlegué a la conclusión por lo siguiente:'),listing(si), listing(no).

borraResp:-retractall(si(_)),retractall(no(_)).

motor:-borraResp,(deduce(Objeto,_) ->
      (nl,write('El sistema infiere que el objeto es: '),write(Objeto),
       writeln(' ¿como la ves?'), explica);
      (nl,write('No hay un objeto con tales atributos en mi base de conocimientos'))).

main:-repeat,
      nl,nl,write('SISTEMA EXPERTO "Cogito Ergo Sum" '),nl,
      nl,write('Menu'),nl,
      nl,write('1 Consulta el sistema experto'),
      nl,write('2 Salir'),
      nl,nl,write('Indica tu opcion:'),
      read(Opcion),nl,
      ( (Opcion=1,motor,fail);
	(Opcion=2,!)).

% BASE DE CONOCIMIENTO

% Reglas del dominio

animal(X) :- satisface(esta_vivo,X),satisface(puede_sentir,X), satisface(puede_moverse,X).
mamifero(X):- animal(X), satisface(da_leche,X).
carnivoro(X):-animal(X),satisface(come_carne,X).
oviparo(X):-animal(X), satisface(pone_huevos,X).
ave(X):-oviparo(X),satisface(tiene_plumas,X).
pez(X):-oviparo(X),satisface(es_acuatico,X).
tigre(X) :- mamifero(X),carnivoro(X),satisface(tiene_rayas,X).
ballena(X):-mamifero(X),carnivoro(X),satisface(es_acuatico,X),satisface(es_grandotota,X).
aguila(X):- ave(X),carnivoro(X),satisface(tiene_garras,X).
tiburon(X):-pez(X), carnivoro(X),satisface(es_muy_feo,X).
vaca(X):-mamifero(X),satisface(tiene_cuernos,X).

% Objetos que puede deducir

deduce(tigre,X)   :- tigre(X).
deduce(ballena,X) :- ballena(X).
deduce(aguila,X)  :- aguila(X).
deduce(tiburon,X) :- tiburon(X).
deduce(vaca,X):- vaca(X).











