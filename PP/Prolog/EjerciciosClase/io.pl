
salida:-write('Mensaje en consola'),writeln(' Mensaje en misma l�nea'),
        write(' El writeln anterior salta a otra l�nea').

entrada:-write('�Cu�l es tu edad? '),
         read(edad). format(' Tienes ~d a�os',edad).

entrada_real:-write('�Cu�l es tu estatura? '),
              read(estatura), format('Mides ~g',estatura).

entrada_varios:-write('Dame tres n�meros: '),read(A), read(B), read(C),
                format('Los valores son ~g ~g ~g'.[A, B, C]).

entrada_texto:-write('Dime tu nombre: '),read(texto),
               format('Tu nombre es: ~s',texto).

cls:-write('[\e[2J').

