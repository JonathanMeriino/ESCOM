clc
clear all
close all
warning off all

a=imread('peppers.png');

b=rgb2gray(a);

minimo=min(min(b));
maximo=max(max(b));

[m,n]=size(b)
intervalo_min=input('dame el valor min del intervalo....=');
intervalo_max=input('dame el valor max del intervalo ....=');

dato1=(intervalo_max-intervalo_min);
dato2=(maximo-minimo);
dato3=(double(dato1) /double(dato2));



for i=1:m
    for j=1:n
        procesada(i,j) = dato3 * (b(i,j) - minimo) + intervalo_min;
        
    end
    
end


figure(1)
subplot(3,2,1)
histogram(b)
title('original histogram')

subplot(3,2,2)
imshow(b)
title('imagen original')


subplot(3,2,3)
histogram(procesada)
title('processed histogram')

subplot(3,2,4)
imshow(procesada)
title('processed histogram')

subplot(3,2,5)
histogram(procesada)
title('histograma ecualizada')

subplot(3,2,6)
imshow(procesada)
title('imagen ecualizada')


disp('fin de proceso...')