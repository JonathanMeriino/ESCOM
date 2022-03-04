clc%Limpia pantalla
clear all %Limpia Todo
close all %Cierra todo
warning off all %Apaga los warning

%empezamos
%lectura de una imagen...

figure(1)
a=imread('cat.jpg');%imread sirve para leer una imagen
%imshow muestra la imagen en otra pantalla
subplot(3,3,1);
imshow(a)
title('original image')

%figure(2)
b=rgb2gray(a);
%imshow(b)
subplot(3,3,2);
imshow(b)
title('gray scale')

%figure(3)
c=imbinarize(b);
%imshow(c)
subplot(3,3,3)
imshow(c)
title('black and white')

%Extraccion de colores de na imagen
%figure(4)
roja = a;
subplot(3,3,4)
roja(:,:,1);
roja(:,:,2)=0;
roja(:,:,3)=0;

imshow(roja)
title('roja')

%figure(5)
verde = a;
subplot(3,3,5)
verde(:,:,1)=0;
verde(:,:,2);
verde(:,:,3)=0;
imshow(verde)
title('verde')

%figure(6)
azul = a;
subplot(3,3,6)
azul(:,:,1)=0;
azul(:,:,2)=0;
azul(:,:,3);

imshow(azul)
title('canal azul')

%Lo paso marco ajajaja imshowpair

%figure(7)
z=[a roja;verde azul];
subplot(3,3,7);
imshow(z)
title('arreglo con todas')
%mezcla aditiva--- mezcla 

figure (2)
yellow = roja + verde;
subplot(3,3,1)
imshow(yellow)
title('amarilla')

magenta = roja + azul;
subplot(3,3,2)
imshow(magenta) 
title('magenta')

cyan= verde + azul;
subplot(3,3,3)
imshow(cyan)
title('Cyan')

% mezcla substractiva: 
blanco = roja+verde+azul;
subplot(3,3,4)
imshow(blanco)
title ('Blanco')

naranja = yellow + roja;
subplot(3,3,5)
imshow(naranja)
title('naranja')

negro = -azul -roja - verde;
subplot(3,3,6)
imshow(negro)
title('negro')

disp("fin de proceso....") %fin de procesode los colores primarios

