close all; clc; clear;

img_rgb = imread('peppers.png');
sz = size (img_rgb);

figure (1)
imshow(img_rgb);
title('Imagen Original');


figure(2);
img_cian = img_rgb;
subplot(2,3,1);
img_cian(:,:,1)=0;
imshow(img_cian);
title('Imagen Cian');

img_mag = img_rgb;
subplot(2,3,2);
img_mag(:,:,2)=0;
imshow(img_mag);
title('Imagen Magenta');

img_yell = img_rgb;
subplot(2,3,3);
img_yell(:,:,3)=0;
imshow(img_yell);
title('Imagen Amarilla');

img_red = img_rgb;
subplot(2,3,4);
img_red(:,:,[2 3])=0;
imshow(img_red);
title('Imagen Roja')

img_blue = img_rgb;
subplot(2,3,5);
img_blue(:,:,[1 2])=0;
imshow(img_blue);
title('Imagen Azul');

img_green = img_rgb;
subplot(2,3,6);
img_green(:,:,[1 3])=0;
imshow(img_green);
title('Imagen Verde');

figure (3)

img_gray = rgb2gray(img_rgb);
subplot(1,2,1);
imshow(img_gray);
title('Imagen Gris')

img_bw = imbinarize(img_gray,"global");
subplot(1,2,2);
imshow(img_bw);
title('Imagen Binarizada');
