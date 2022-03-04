clc
clear all
close all
warning of all
% Practica 1 - Procesamiento digital de imagenes

figure(1)
% imagen original
a = imread('cat.jpg'); % lee la imagen  a ocupar
% mostramos y colocamos titulo a la imagen original
imshow(a)  
title('original image')

sz = size(a); % regresa un vector con las dimensiones de a

figure(2)

% Parte A de la practica
picture1=a
subplot(2,2,1) % matriz de 2x2 y lo colocamos en la imagen 1
picture1(1:390,1:520,1); % muestra el color original
picture1(1:390,521:1040,1)=0; % valor uno es cian
picture1(391:780,1:520,2)=0; %  %valor dos es guinda
picture1(391:780,521:1040,3)=0; %valor tres es amarilla
imshow(picture1);
title('Parte A')
%Parte B 
picture2=a;
subplot(2,2,2)
picture2(:,1:346,[2 3])=0; % color rojo
picture2(:,347:693,[1 3])=0; % color verde
picture2(:,694:1040,[1 2])=0;%color azul
imshow(picture2);
title('Parte B')
%Parte C
picture3=a;
subplot(2,2,3)
picture3(1:260,:,[2 3])=0;
picture3(261:520,:,[1 3])=0;
picture3(521:780,:,[1 2])=0;
imshow(picture3);
title('Parte C')
Parte D
picture4=a;
subplot(2,2,4)
picture4(60:576,470:530,[1 3])=0; %G
picture4(60:120,258:742,[1 3])=0; %G
picture4(516:576,258:742,[1 3])=0; %G

picture4(1:780,1:257,[2 3])=0; %R
picture4(121:515,258:469,[2 3])=0; %R
picture4(1:59,258:519,[2 3])=0; %R
picture4(577:780,258:519,[2 3])=0; %R

picture4(1:780,743:1040,[1 2])=0; %B
picture4(121:515,531:742,[1 2])=0; %B
picture4(1:59,520:742,[1 2])=0; %B
picture4(577:780,520:742,[1 2])=0; %B
imshow(picture4);
title('Parte D')
