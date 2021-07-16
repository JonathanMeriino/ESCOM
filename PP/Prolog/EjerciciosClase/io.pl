
salida:-write('Mensaje en consola'),writeln(' Mensaje en misma línea'),
        write(' El writeln anterior salta a otra línea').

entrada:-write('¿Cuál es tu edad? '),
         read(edad). format(' Tienes ~d años',edad).

entrada_real:-write('¿Cuál es tu estatura? '),
              read(estatura), format('Mides ~g',estatura).

entrada_varios:-write('Dame tres números: '),read(A), read(B), read(C),
                format('Los valores son ~g ~g ~g'.[A, B, C]).

entrada_texto:-write('Dime tu nombre: '),read(texto),
               format('Tu nombre es: ~s',texto).

cls:-write('[\e[2J').

