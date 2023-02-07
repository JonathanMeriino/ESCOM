close all; clc; clear;

%lectura de la imagen original
im = imread("Images\img1.jpg");

%mostar imagen original
imshow(im)

%valores de color de los pixeles
pix = impixel(im,500,500)
%seleccionamos el pixel a analizar
pix2 = impixel(im)

%Realizar el corte de una imagen
corte = imcrop(im)
imshow(corte);