
main:- bienvenida, evaluar.

bienvenida:-writeln('\nConsultorio del Dr. Hacker, vamos a evaluar la PC').
evaluar:-
hipotesis(Problema),
write('La computadora tiene el problema de '),
write(Problema),
nl,
write('Llevala a mantenimiento!'),
deshacer.

% Hipotesis que deberia ser probada
hipotesis(fallo_so) :- fallo_so.
hipotesis(fallo_ram) :- fallo_ram.
hipotesis(fallo_discoDuro) :- fallo_discoDuro.
hipotesis(falla_rom) :- falla_rom.
hipotesis(tiene_virus) :- tiene_virus.
hipotesis(desconocido).

% Reglas de identificacion
fallo_so :-
verificar(pantalla_azul),
verificar(bajo_rendi),
verificar(perdida_info),
verificar(demora_inicio),
write('Consejos y Sugerencias:'),
nl,
write('1: Reinicie el software'),
nl,
write('2: Libere la memoria ram '),
nl,
write('3: Vuelva a instalar el sistema'),
nl,
write('Si el problema persiste, traigala de nuevo'),
nl.

fallo_ram :-
verificar(solo_apaga),
verificar(pantalla_azul),
verificar(perdida_info),
verificar(demora_inicio),
write('Consejos y Sugerencias:'),
nl,
write('1: Apagar el PC'),
nl,
write('2: Probar los modulos '),
nl,
write('3: Limpiar la memoria ram'),
nl,
write('Si el problema persiste, traigala de nuevo'),
nl.

fallo_discoDuro :-
verificar(pantalla_azul),
verificar(perdida_info),
verificar(demora_inicio),
verificar(solo_apaga),
write('Consejos y Sugerencias:'),
nl,
write('1: Hay que reparar la unidad '),
nl,
write('2: Se puede adquirir un nuevo disco'),
nl,
write('3: Limpieza de hardware'),
nl,
write('4: Revise el antivirus'),
nl,
write('Si el problema persiste,traigala de nuevo'),
nl.

fallo_rom :-
verificar(solo_apaga),
verificar(perdida_info),
verificar(demora_inicio),
verificar(publicidad),
write('Consejos y Sugerencias:'),
nl,
write('1: Limpiar la entrada con cuidado'),
nl,
write('2: Reinicie la computadora'),
nl,
write('3: Verificar si esta bien colocada'),
nl,
write('4: Verificar que funcionen todos sus circuitos'),
nl,
write('Si el problema persiste, traigala de nuevo'),
nl.

tiene_virus :-
verificar(solo_apaga),
verificar(perdida_info),
verificar(pantalla_azul),
verificar(demora_inicio),
verificar(publicidad),
verificar(bajo_rendi),
write('Consejos y Sugerencias:'),
nl,
write('1: Instalar un antivirus'),
nl,
write('2: Elimine los programas sospechosos'),
nl,
write('3: Inicie el equipo en modo seguro'),
nl,
write('4: Haga una copia de seguridad y restaure a fabrica'),
nl,
write('Si el problema persiste, traigala de nuevo'),
nl.

% Como se hacen las preguntas 
preguntar(Pregunta) :-
write('La computadora tiene el siguiente fallo:'),
write(Pregunta),
write('? '),
read(Respuesta),
nl,
( (Respuesta == si)
->
assert(si(Pregunta)) ;
assert(no(Pregunta)), fail).

:- dynamic si/1,no/1.
% Como se verifica 
verificar(S) :-
(si(S)
->
true ;
(no(S)
->
fail ;
preguntar(S))).


% deshacer all si/no assertions
deshacer :- retract(si(_)),fail.
deshacer :- retract(no(_)),fail.
deshacer.






