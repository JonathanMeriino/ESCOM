clc
clear all
close all
warning of all

b=imread('peppers.png');
%figure(3)
%imshow(b);
%imhist(b);

roja=b;
roja(:,:,1);
roja(:,:,2)=0;
roja(:,:,3)=0;
%imshow(roja);

verde=b;
verde(:,:,1)=0;
verde(:,:,2);
verde(:,:,3)=0;
%imshow(verde);

azul=b;
azul(:,:,1)=0;
azul(:,:,2)=0;
azul(:,:,3);
%imshow(azul);

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

MIN = 0;
MAX = 255;
opcion = 1;

while opcion == 1
minimo = input('Ingrese valor minimo: ');
maximo= input('Ingrese valor maximo: ');

variableX= (MAX - MIN);
variableY= (maximo - minimo);
variableZ= (double(variableY)/double(variableX));

for i = 1:384
    for j = 1:512
        new_roja(i,j) = (roja_r(i,j)-MIN)*variableZ + minimo;
        
        new_verde(i,j) = (verde_r(i,j)-MIN)*variableZ + minimo;
        
        new_azul(i,j) = (azul_r(i,j)-MIN)*variableZ + minimo;
    end
end
figure(2)
%R
subplot(2,3,1);
imshow(new_roja);
title('imagen roja new');
subplot(2,3,4);
histogram(new_roja);
title('histograma rojo new');
%G
subplot(2,3,2);
imshow(new_verde);
title('imagen verde new');
subplot(2,3,5);
histogram(new_verde);
title('histograma verde new');

%B
subplot(2,3,3);
imshow(new_azul);
title('imagen azul new');
subplot(2,3,6);
histogram(new_azul);
title('histograma azul new');
opcion = input('Desea comprimir o expandir nuevamente (1.- SI, 2.- NO):');
end