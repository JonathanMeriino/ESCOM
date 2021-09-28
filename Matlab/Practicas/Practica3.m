% Practica 3 - Ecualizacion y correspondencia de una imagen
clc;
clear all;
close all;
warning of all;

original=imread('peppers.png');
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
imshow(procesada);
procesada= uint8(procesada);

figure(1)
subplot(2,1,1)
imshow(procesada);
title('procesada');

subplot(2,1,2)
imhist(procesada);
title('procesada');
%inicio de ecualizada
nuevo_max = max(max(procesada));
nuevo_min = min(min(procesada));

[x,y]=size(procesada);
g = unique(procesada);
tam = size(g);

cantidad_numero=zeros(tam);
proba=zeros(tam);
acumulada=zeros(tam);
Eq =zeros(tam);
%hola = tam(1);
suma = 0;
for i=1:tam(1)
    repetido = numel(find(procesada == g(i))); %cuantas veces se repire el numero de gris
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
figure(2)
subplot(2,1,1)
imshow(ecualizada);
title('ecualizada');

subplot(2,1,2)
imhist(ecualizada);
title('ecualizada');


% fin de ecualizada

%tabla de imagen ya ecualizada
ecua_max = max(max(ecualizada));
ecua_min = min(min(ecualizada));

[m,n]=size(ecualizada);
Eg = unique(ecualizada);
Etam = size(Eg);

cantidad_numero_ecu=zeros(Etam);
proba2=zeros(Etam);
acumulada2=zeros(Etam);
Eq =zeros(Etam);
hola = Etam(1);
suma2 = 0;
for i=1:Etam(1)
    repetido2 = numel(find(ecualizada == Eg(i))); 
    cantidad_numero_ecu(i) = repetido2;
    suma2 = repetido2 + suma2;
    proba2(i) = (double(cantidad_numero_ecu(i))/double(m*n));
    acumulada2(i) = (double(suma2)/double(m*n));
end

tab = table(Eg,cantidad_numero_ecu, proba2, acumulada2)


%correspondencia
g2 = zeros(Etam);
i = 1;
N = 1;
for Q = 1:Etam(1)
    for W = 1:tam(1)
        acumulada(W,N);
        acumulada2(Q,N);
        if (acumulada2(Q,N) <= acumulada(W,N))
                g2(i) = W;
                i = i + 1;
                Q = Q + 1;
                W = 1;
                break
        end
    end
end

corr = table(g2)

for j=1:m
    for k=1:n
        for T=1:Etam(1)
            if ecualizada(j,k) == Eg(T);
                correspondencia(j,k) = g2(T,N);
            end
        end
    end
end
correspondencia = uint8(correspondencia);
figure(3)
subplot(2,1,1)
imshow(correspondencia);
title('correspondencia');

subplot(2,1,2)
imhist(correspondencia);
title('correspondencia');
