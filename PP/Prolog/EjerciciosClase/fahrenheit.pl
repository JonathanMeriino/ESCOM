
main:-cls,writeln('Programa para Convertir de grados Celsius a grados Fahrenheit'),
      write('\nIndique los grados Celsius: '), read(C),
      F is C*1.8+32,
      format('\n ~g °C equivalen a ~g °F',[C, F]).

cls:-write('[\e[2J').
