%Practica 2 - Expansion del histograma
clc
clear all
close all
warning of all

b=imread('peppers.png');

roja=b;
roja(:,:,[2 3])=0;

verde=b;
verde(:,:,[1 3])=0;

azul=b;
azul(:,:,[1 2])=0;

figure(1)
% imagen roja antes de expansion
rojaGris=roja(:,:,1); %roja escala de grises
subplot(3,3,1)
imshow(roja);
title('Imagen roja');
subplot(3,3,4)
imshow(rojaGris); 
title('Imagen gris-roja');
subplot(3,3,7)
histogram(rojaGris);
title('Histograma gris-roja');
%imagen verde antes de expansion
verdeGris=verde(:,:,2); %verde escala de grises
subplot(3,3,2)
imshow(verde);
title('Imagenverde');
subplot(3,3,5)
imshow(verdeGris);
title('Imagen gris-verde')
subplot(3,3,8)
histogram(verdeGris);
title('Histograma gris-verde')
%imagen azul antes de expansion
azulGris=azul(:,:,3); %azul escala de grises
subplot(3,3,3)
imshow(azul);
title('Imagen azul');
subplot(3,3,6)
imshow(azulGris);
title('Imagen gris-azul');
subplot(3,3,9)
histogram(azulGris);
title('Histograma gris-azul');
%minimo y maximos deseados
MIN = 0; 
MAX = 255;
opcion = 1;

while opcion == 1
% minimo y maximo añadidos por el usuario
minimo = input('Ingrese valor minimo: ');
maximo= input('Ingrese valor maximo: ');
%formula para calcular la expancion del histogrma
variableX= (MAX - MIN);
variableY= (maximo - minimo);
variableZ= (double(variableY)/double(variableX));
%recorrido de i filas y j columnas
for i = 1:384
    for j = 1:512
        expRoja(i,j) = (rojaGris(i,j)-MIN)*variableZ + minimo; % nueva imagen roja
        
        expVerde(i,j) = (verdeGris(i,j)-MIN)*variableZ + minimo; % nueva imagen verde
         
        expAzul(i,j) = (azulGris(i,j)-MIN)*variableZ + minimo; %nueva imagen azul
    end
end

figure(2)
%Red
subplot(2,3,1);
imshow(expRoja);
title('Nueva imagen R');
subplot(2,3,4);
histogram(expRoja);
title('Nuevo Histograma R');
%Green
subplot(2,3,2);
imshow(expVerde);
title('Nueva imagen G');
subplot(2,3,5);
histogram(expVerde);
title('Nueva Histograma G');
%Blue
subplot(2,3,3);
imshow(expAzul);
title('Nueva imagen B');
subplot(2,3,6);
histogram(expAzul);
title('Nueva Histograma B');

opcion = input('Desea comprimir o expandir nuevamente (1.- SI, 2.- NO):');
end