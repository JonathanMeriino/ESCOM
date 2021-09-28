clc;
clear;

original=imread('gato.jpeg');
originalGrises = rgb2gray(original);

minimo=min(min(originalGrises));
maximo=max(max(originalGrises));

[m,n]=size(originalGrises)
intervalo_min=input('Ingresa el valor del intervalo minimo: ');
intervalo_max=input('Ingresa el valor del intervalo maximo: ');

dato1=(intervalo_max-intervalo_min);
dato2=(maximo-minimo);
dato3=(double(dato1) /double(dato2));

for i=1:m
    for j=1:n
        procesada(i,j) = dato3 * (originalGrises(i,j) - minimo) + intervalo_min;
        
    end
    
end

procesada= uint8(procesada);

nuevo_max = max(max(procesada));
nuevo_min = min(min(procesada));

[x,y]=size(procesada);
g = unique(procesada);
tam = size(g);

cantidad_numero=zeros(tam);
proba=zeros(tam);
acumulada=zeros(tam);
Eq =zeros(tam);

suma = 0;
for i=1:tam(1)
    repetido = numel(find(procesada == g(i))); %cuantas veces se repite el numero de gris
    cantidad_numero(i) = repetido;
    suma = repetido + suma;
    proba(i) = (double(cantidad_numero(i))/double(x*y));
    acumulada(i) = (double(suma)/double(x*y));
    Eq(i) = (nuevo_max - nuevo_min)*acumulada(i) + nuevo_min;
end

tab = table(g,cantidad_numero, proba, acumulada, Eq)

for j=1:x
    for k=1:y
        for T=1:i
            if procesada(j,k) == g(T);
                ecualizada(j,k) = Eq(T);
            end
        end
    end
end
ecualizada = uint8(ecualizada);


subplot(3,2,1)
imshow(original);
title('Imagen original')

subplot(3,2,2)
imhist(original);
title('Histograma Original');

subplot(3,2,3)
imshow(procesada);
title('Imagen procesada');
subplot(3,2,4)
histogram(procesada);
title('Histograma procesada');

subplot(3,2,5)
imshow(ecualizada);
title('Imagen ecualizada');

subplot(3,2,6)
histogram(ecualizada);
title('Histograma ecualziado');

figure(2)

corres = imhistmatch(ecualizada, procesada);
imshow(corres)
