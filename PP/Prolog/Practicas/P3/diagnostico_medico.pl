
:- dynamic conocido/1.

main:-bienvenida,limpia_memoria_de_trabajo,consulta.

bienvenida:-writeln('\nConsultorio del Dr. Simio'), writeln('\nLe haré algunas preguntas\n').

consulta:-haz_diagnostico(X),escribe_diagnostico(X),ofrece_explicacion_diagnostico(X).
consulta:-write('No hay suficiente conocimiento para elaborar un diagnostico.').

haz_diagnostico(Diagnosis):-obten_hipotesis_y_sintomas(Diagnosis, ListaDeSintomas),
	        prueba_presencia_de(Diagnosis, ListaDeSintomas).

obten_hipotesis_y_sintomas(Diagnosis, ListaDeSintomas):-frame(enfermedad(Diagnosis), sintomas(ListaDeSintomas)).

prueba_presencia_de(_, []).
prueba_presencia_de(Diagnosis, [Head | Tail]):- prueba_verdad_de(Diagnosis, Head),prueba_presencia_de(Diagnosis, Tail).

prueba_verdad_de(_, Sintoma):- conocido(Sintoma).

prueba_verdad_de(Diagnosis, Sintoma):- not(conocido(is_false(Sintoma))),
	                               pregunta_sobre(Diagnosis, Sintoma, Reply),
				       Reply = si.

pregunta_sobre(Diagnosis, Sintoma, Reply):- write('Es verdad que usted '),
	                                    write(Sintoma), write('? '),
					    read(Respuesta),
					    process(Diagnosis, Sintoma, Respuesta, Reply).

process(_, Sintoma, si, si):- asserta(conocido(Sintoma)).
process(_, Sintoma, no, no):- asserta(conocido(is_false(Sintoma))).
process(Diagnosis, Sintoma, porque, Reply):- nl,
write('Estoy investigando la hipotesis siguiente: '),
write(Diagnosis), write('.'), nl, write('Para esto necesito saber si '),
write(Sintoma), write('.'), nl, pregunta_sobre(Diagnosis, Sintoma, Reply).
process(Diagnosis, Sintoma, Respuesta, Reply):- Respuesta \== no,
Respuesta \== si, Respuesta \== porque, nl,
write('Debes contestar si, no o porque.'), nl,
pregunta_sobre(Diagnosis, Sintoma, Reply).

escribe_diagnostico(Diagnosis):- write('El diagnostico es '),
write(Diagnosis), write('.'), nl.


ofrece_explicacion_diagnostico(Diagnosis):-
pregunta_si_necesita_explicacion(Respuesta),
actua_consecuentemente(Diagnosis, Respuesta).
pregunta_si_necesita_explicacion(Respuesta):-
write('Quieres que justifique este diagnostico? '),
read(RespuestaUsuario),
asegura_respuesta_si_o_no(RespuestaUsuario, Respuesta).


asegura_respuesta_si_o_no(si, si).
asegura_respuesta_si_o_no(no, no).
asegura_respuesta_si_o_no(_, Respuesta):- write('Debes contestar si o no.'),
pregunta_si_necesita_explicacion(Respuesta).
actua_consecuentemente(_, no).
actua_consecuentemente(Diagnosis, si):- frame(enfermedad(Diagnosis), sintomas(ListaDeSintomas)),
		      write('Se determino este diagnostico porque se encontraron los siguentes sintomas: '), nl,
                       escribe_lista_de_sintomas(ListaDeSintomas).
escribe_lista_de_sintomas([]).
escribe_lista_de_sintomas([Head | Tail]):-write(Head), nl, escribe_lista_de_sintomas(Tail).


limpia_memoria_de_trabajo:- retractall(conocido(_)).

frame(enfermedad('gastritis'),
      sintomas(['tiene dolor agudo en vientre',
                'tiene diarrea',
                'tiene muchos gases'])).
frame(enfermedad('sarampion'),
      sintomas(['esta cubierto de puntos',
		'tiene temperatura alta',
                'tiene ojos rojos',
		'tiene tos seca'])).
frame(enfermedad('malaria'),
      sintomas(['tiene temperatura alta',
		'tiene dolor en las articulaciones',
		'tiembla violentamente',
		'tiene escalofrios'])).
frame(enfermedad('influenza'),
      sintomas(['tiene dolor en las articulaciones',
	        'tiene mucho estornudo',
                'tiene dolor de cabeza'])).
frame(enfermedad('gripe'),
      sintomas(['tiene cuerpo cortado',
                'tiene dolor de cabeza',
	        'tiene temparatura alta'])).
frame(enfermedad('tifoidea'),
      sintomas(['tiene falta de apetito',
		'tiene temperatura alta',
		'tiene dolor abdominal',
		'tiene dolor de cabeza',
		'tiene diarrea'])).











