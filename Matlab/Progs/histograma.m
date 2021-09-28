clc
clear all
close all
warning of all

a = imread('cameraman.tif');
imshow(a)
[m,n] = size(a);
figure(2)
[veces,pixeles]= imhist(a)
imhist(a)


b = imread('peppers.png')
figure(3)
imshow(b)
imhist(b)

roja = b;

roja(:,:,1);
roja(:,:,2)=0;
roja(:,:,3)=0;
imshow(roja);

verde = b;

verde(:,:,1)=0;
verde(:,:,2);
verde(:,:,3)=0;
imshow(verde);

azul = b;

azul(:,:,1)=0;
azul(:,:,2)=0;
azul(:,:,3);
imshow(azul);

figure(4)
roja_r=roja(:,:,1);
subplot(1,3,1)
imshow(roja)
subplot(1,3,2)
imshow(roja_r);
subplot(1,3,3)
%imhist(roja_r)
histogram(roja_r)

figure(5)
verde_r=verde(:,:,2);
subplot(1,3,1)
imshow(verde);
subplot(1,3,2)
imshow(verde_r)
%imhist(verde_r)
subplot(1,3,3)
histogram(verde_r)

figure(6)
azul_r=azul(:,:,3);
subplot(1,3,1)
imshow(azul);
subplot(1,3,2)
imshow(azul_r)
%imhist(verde_r)
subplot(1,3,3)
histogram(azul_r)



disp ('Fin del proceso')