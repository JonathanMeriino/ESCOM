clc;
clear all;
close all;


original=imread('lena.bmp');
originalGrises = original;
%original=imread('arbol.jpg');
%originalGrises = rgb2gray(original);

[m,n]=size(originalGrises);
tam = size(originalGrises);
matriz_prediccion = zeros(tam);

%llenado de primera columna y fila
for i=1:m
    for j=1:n
        if (i == 1)
           matriz_prediccion(i,j) = originalGrises(i,j);
        end
        if (j == 1)
            matriz_prediccion(i,j) = originalGrises(i,j);
        end
    end
end

inicial_prediccion = matriz_prediccion;
suma = 0;
contador = 0;

%llenar datos en prediccion
for i=2:m
    for j=2:n
        if (matriz_prediccion(i,j) == 0)
            suma = matriz_prediccion(i-1,j-1);%primera posicion
            contador = contador + 1;

            suma = suma + matriz_prediccion(i,j-1);%segunda posicion
            contador = contador + 1;

            if (i < m)
                suma = suma + matriz_prediccion(i+1,j-1);%tercera posicion
                contador = contador + 1;
            end

            suma = suma + matriz_prediccion(i-1,j);%cuarta posicion
            contador = contador + 1;

            if (j < n)
                suma = suma + matriz_prediccion(i-1,j+1);%sexta posicion
                contador = contador + 1;
            end
            promedio = round(suma/contador);
            matriz_prediccion(i,j) = promedio;
            suma = 0;
            contador = 0;
            promedio = 0;
        end
    end
end

%resta de imagenes para matriz de error
matriz_error = zeros(tam);

for i=1:m
    for j=1:n
        matriz_error(i,j) = (originalGrises(i,j) - matriz_prediccion(i,j));
    end
end

minimo=min(min(matriz_error));
maximo=max(max(matriz_error));

pixeles = input('Ingresa el numero de bit/pixel: ');

numero_muestra = 2^(pixeles);

theta = (maximo-minimo)/numero_muestra;
numeros = zeros(m,2);
acumulado = 0;
posicion = 0;

%llenar rangos y posiciones
for i=1:(numero_muestra)
    acumulado = acumulado + (minimo + theta);
    numeros(i,1) = acumulado;
    numeros(i,2) = posicion;
    posicion = posicion + 1;
end  

MEQ = zeros(tam);

%llenar MEQ
for i=1:m
    for j=1:n
        for k=1:numero_muestra
            if(matriz_error(i,j) <= numeros(k,1))
                MEQ(i,j) = numeros(k,2);
                break
            end
        end
    end
end

MEQ_inversa = zeros(tam);

%llenar MEQ_inversa 
for i=1:m
    for j=1:n
        for k=1:numero_muestra
            if (MEQ(i,j) == numeros(k,2))
                if (numeros(k,2) == 0)
                    intervalo2 = numeros(k,1);
                    operacion = (intervalo2)/2;
                    MEQ_inversa(i,j) = operacion;
                else
                    intervalo1 = numeros(k-1,1);
                    intervalo2 = numeros(k,1);
                    operacion = (intervalo1+intervalo2)/2;
                    MEQ_inversa(i,j) = operacion;
                end
            end
        end
    end
end


ImagenRecuperada = round(MEQ_inversa + matriz_prediccion);
ImagenRecuperada = uint8(ImagenRecuperada);


figure(1)
subplot(1,2,1)
imshow(originalGrises);
title('Original');
subplot(1,2,2)
imshow(ImagenRecuperada);
title('Imagen Recuperada');

suma_original_total = 0;
resta_original_total = 0;

%sumatoria para operacion señal de ruido
for i=1:m
    for j=1:n
        suma_original = double(originalGrises(i,j)^2);
        suma_original_total = suma_original_total + suma_original;
        
        resta_original = double((originalGrises(i,j) - ImagenRecuperada(i,j))^2);
        resta_original_total = resta_original_total + resta_original;
        
    end
end

s_ruido = 10 * log10((suma_original_total)/(resta_original_total))
