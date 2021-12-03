entrada:-write('Ingrese Numero 1: ') , read(X),
         write('Ingrese Numero 2: '), read(Y).

menor(X,Y):- (
        (X<Y, write(X) , write('Es el menor y'), write(Y),write('Es el mayor')); 
        (X>Y, write(X), write('Es el mayor'), write(Y),write('Es el menor')).  
