% Practica 3 - Ecualizacion y correspondencia de una imagen
clc;
clear all;
close all;
warning of all;

original=imread('peppers.png');
originalGrises = rgb2gray(original); % conversion de una imagen rgb a escala de grises

% retorna el valor minimo y maximo de la imagen a escala de grises
minimo=min(min(originalGrises));
maximo=max(max(originalGrises));

[m,n]=size(originalGrises); % retorna el tamaño de la imagen en m filas y n columnas
% intervalos minimo y maximos por entrada de usuario
intervalo_min=input('Ingresa el valor del intervalo minimo: ');
intervalo_max=input('Ingresa el valor del intervalo maximo: ');
% Proceso para expansion del histograma
variableX=(maximo-minimo);
variableY=(intervalo_max-intervalo_min);
variableZ=(double(variableY) /double(variableX));
% recorrido de la imagen por m filas y n columnas
for i=1:m
    for j=1:n
        procesada(i,j) = (originalGrises(i,j) - minimo)*variableZ + intervalo_min; 
        
    end
    
end
% unit8 - > matrices de enteros sin signo de 8 bits
procesada= uint8(procesada);

figure(1)
subplot(1,2,1)
imshow(procesada);
title('Imagen Procesada');
subplot(1,2,2)
histogram(procesada);
title('Histograma Procesada');


%inicio de ecualizacion

% minimos y maximos de la imagen procesada
proc_max = max(max(procesada));
proc_min = min(min(procesada));

[x,y]=size(procesada);  % retorna el tamaño de la imagen en x filas y y columnas 
g = unique(procesada); % devuelve los mismos datos en procesada sin repetirse y ordenados
tam = size(g); % retorna el tamaño de g y se almacena en tam

%declaracion de matrices de ceros de tamaño tam 
cantidad_numero=zeros(tam);
proba=zeros(tam);
acumulada=zeros(tam);
Eq =zeros(tam);
suma = 0;
% Proceso que calcula la probabilidad Acumulada
for i=1:tam(1)
    repetido = numel(find(procesada == g(i))); %cuantas veces se repire el numero de gris
    cantidad_numero(i) = repetido;
    suma = repetido + suma;
    proba(i) = (double(cantidad_numero(i))/double(x*y));
    acumulada(i) = (double(suma)/double(x*y));
    Eq(i) = (proc_max - proc_min)*acumulada(i) + proc_min; % ecuacion de ecualizacion
end
%tabla de imagen ya ecualizada
tab = table(g,cantidad_numero, proba, acumulada, Eq)

for j=1:x
    for k=1:y
        for T=1:i
            if procesada(j,k) == g(T);
                ecualizada(j,k) = Eq(T); %asigna los valores a ecualizada
            end
        end
    end
end
% unit8 - > matrices de enteros sin signo de 8 bits
ecualizada = uint8(ecualizada);

figure(2)
subplot(1,2,1)
imshow(ecualizada);
title('Imagen Ecualizada');

subplot(1,2,2)
histogram(ecualizada);
title('Histograma Ecualizada');


% Fin proceso de ecualizacion


% Proceso de correspondencia

% minimos y maximos de la imagen ecualizada

ecua_max = max(max(ecualizada));
ecua_min = min(min(ecualizada));

[m,n]=size(ecualizada);  % retorna el tamaño de la imagen en x filas y y columnas 
Eg = unique(ecualizada);  % devuelve los mismos datos en ecualizada sin repetirse y ordenados
Etam = size(Eg);   % retorna el tamaño de Eg y se almacena en Etam
%declaracion de matrices de ceros de tamaño Etam 
cantidad_numero_ecu=zeros(Etam);
proba2=zeros(Etam);
acumulada2=zeros(Etam);
Eq =zeros(Etam);
suma2 = 0;
%proceso que calcula la probabilidad acumulada
for i=1:Etam(1)
    repetido2 = numel(find(ecualizada == Eg(i))); %cuantas veces se repire el numero de gris
    cantidad_numero_ecu(i) = repetido2;
    suma2 = repetido2 + suma2;
    proba2(i) = (double(cantidad_numero_ecu(i))/double(m*n));
    acumulada2(i) = (double(suma2)/double(m*n));
end
%tabla de imagen acumulada
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
%tabla de correspondencia
corr = table(g2)

for j=1:m
    for k=1:n
        for T=1:Etam(1)
            if ecualizada(j,k) == Eg(T);
                correspondencia(j,k) = g2(T,N); %asigna los valores a correspondencia
            end
        end
    end
end
% unit8 - > matrices de enteros sin signo de 8 bits
correspondencia = uint8(correspondencia);
figure(3)
subplot(1,2,1)
imshow(correspondencia);
title('Imagen correspondencia');

subplot(1,2,2)
histogram(correspondencia);
title('Histograma correspondencia');
