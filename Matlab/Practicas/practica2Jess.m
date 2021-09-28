clc
clear all
close all
warning of all

b=imread('peppers.png');

roja=b;
roja(:,:,1);
roja(:,:,2)=0;
roja(:,:,3)=0;

verde=b;
verde(:,:,1)=0;
verde(:,:,2);
verde(:,:,3)=0;

azul=b;
azul(:,:,1)=0;
azul(:,:,2)=0;
azul(:,:,3);

figure(1)
roja_r=roja(:,:,1);
subplot(3,3,1)
imshow(roja);
title('imagen roja');
subplot(3,3,4)
imshow(roja_r);
title('imagen gris roja');
subplot(3,3,7)
histogram(roja_r);
title('histograma gris roja');

verde_r=verde(:,:,2);
subplot(3,3,2)
imshow(verde);
title('imagen verde');
subplot(3,3,5)
imshow(verde_r);
title('imagen gris verde')
subplot(3,3,8)
histogram(verde_r);
title('histograma gris verde')

azul_r=azul(:,:,3);
subplot(3,3,3)
imshow(azul);
title('imagen azul');
subplot(3,3,6)
imshow(azul_r);
title('imagen gris azul');
subplot(3,3,9)
histogram(azul_r);
title('histograma gris azul');

opcion = 1;
while opcion == 1
figure(2)
minimo = input('Ingrese valor minimo: ');
maximo= input('Ingrese valor maximo: ');

fmin = 0;
fmax=255;

for i = 1:384
    for j = 1:512
        
        
    adjRed(i,j)= (roja_r(i,j)-fmin)*((maximo-minimo)/(fmax-fmin))+minimo;
    adjGreen(i,j) = (verde_r(i,j)-fmin)*((maximo-minimo)/(fmax-fmin))+minimo;
    adjBlue(i,j) = (azul_r(i,j)-fmin)*((maximo-minimo)/(fmax-fmin))+minimo;
     
    end
end
subplot(3,3,1)
imshow(roja_r);
title('imagen gris roja');

subplot(3,3,2)
imshow(verde_r);
title('imagen gris verde');

subplot(3,3,3)
imshow(azul_r);
title('imagen gris azul');
%R
subplot(3,3,4);
imshow(adjRed);
title('imagen roja new');
subplot(3,3,7);
imhist(adjRed);
title('histograma rojo new');
%G
subplot(3,3,5);
imshow(adjGreen);
title('imagen verde new');
subplot(3,3,8);
histogram(adjGreen);
title('histograma verde new');

%B
subplot(3,3,6);
imshow(adjBlue);
title('imagen azul new');
subplot(3,3,9);
histogram(adjBlue);
title('histograma azul new');

opcion = input('Desea comprimir o expandir nuevamente (1.- SI, 2.- NO):');
end

imtool(roja_r)
disp ('Fin del proceso')
