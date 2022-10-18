#include <opencv2/opencv.hpp>
#include <stdio.h>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <stdint.h>
/////////////////////////////////////////////////////////////////////////////

///////////////////////////////Espacio de nombres////////////////////////////
using namespace cv;
using namespace std;
/////////////////////////////////////////////////////////////////////////////


/////////////////////////Inicio de la funcion principal///////////////////
int main()
{

	/********Declaracion de variables generales*********/
	char NombreImagen[] = "lenna.png";
	Mat imagen; // Matriz que contiene nuestra imagen sin importar el formato
	//Creacion de las matrices para almacenar nuestras imagnes
	Mat i_fun;  
	Mat i_prom;
	Mat i_ntsc;
	/************************/

	/*********Lectura de la imagen*********/
	imagen = imread(NombreImagen);
	// imagen.data obtiene el contenido internamente de un objeto
	if (!imagen.data)
	{
		cout << "Error al cargar la imagen: " << NombreImagen << endl;
		exit(1);
	}
	/************************/

	/************Procesos*********/
	int fila_original = imagen.rows; //lectura de numero de filas
	int columna_original = imagen.cols;//Lectura de numero de columnas
	uint8_t array[fila_original][columna_original]; // creacion del array 
	// uint8_t : tipo de 8 bits sin signos 

	cout << "filas: " << fila_original << endl;
	cout << "columnas: " << columna_original << endl;

	namedWindow("Hola Mundo", WINDOW_AUTOSIZE);//Creación de una ventana
	imshow("Hola Mundo", imagen);
	
	/*Convertir la imagen de RGB a escala de grises (Funcion)*/

	cvtColor(imagen, i_fun, COLOR_BGR2GRAY); //Implementacion de la funcion (funcion original, donde se almacena , metodo)

	
	imshow("Escala de grises con funcion", i_fun); //Impresion de la imagen en escala de grises

	/*Convertir la imagen de RGB a escala de grises (Promedio)*/
	
	// Ciclo donde se almacenan los indices 
	for (int i = 0; i < fila_original; i++) {
		for (int j = 0; j < columna_original; j++) {
			array[i][j] = 0;
		}
	}
	// Apuntador a la direccion de memoria de los datos contenidos en la imagen
	uint8_t* pixelApt = (uint8_t*)imagen.data;
	
	int canal = imagen.channels(); //Almacenamos el numero de canales en la variable cn

	Scalar_<uint8_t> bgrPixel; //Creamos un vector escalar de tipo uint8_t

	for (int i = 0; i < fila_original; i++)

	{
		for (int j = 0; j < columna_original; j++)
		{

			bgrPixel.val[0] = pixelApt[i * imagen.cols * canal + j * canal + 0]; // Azul

			bgrPixel.val[1] = pixelApt[i * imagen.cols * canal + j * canal + 1]; // Verde

			bgrPixel.val[2] = pixelApt[i * imagen.cols * canal + j * canal + 2]; // Rojo

			int promedio = (bgrPixel.val[0] + bgrPixel.val[1] + bgrPixel.val[2]) / 3; // calculo del promedio de los 3 canales

			array[i][j] = promedio;
		}
	}
	
	Mat i_prom(Size(fila_original, columna_original), CV_8UC1, array, Mat::AUTO_STEP); // implementacion metodo promedidada
	// CV_8U1 : Es una matriz de un solo canal de 8 bits que se utiliza principalmente para almacenar y obtener los valores de cualquier imagen
	// Mat:: AUTO_STEP
	
	imshow("Gris Promedio", i_prom); // Se muestra la imagen en escala de grises metodo promediada
	/*Convertir la imagen de RGB a escala de grises (NTSC)*/

	for (int i = 0; i < fila_original; i++) {
		for (int j = 0; j < columna_original; j++) {
			array[i][j] = 0;
		}
	}
	// Apuntador a la direccion de memoria de los datos contenidos en la imagen
	uint8_t* pixelApt = (uint8_t*)imagen.data;
	
	int canal = imagen.channels(); //Almacenamos el numero de canales en la variable cn

	Scalar_<uint8_t> bgrPixel; //Creamos un vector escalar de tipo uint8_t

	for (int i = 0; i < fila_original; i++)

	{
		for (int j = 0; j < columna_original; j++)

		{
			bgrPixel.val[0] = pixelApt[i * imagen.cols * canal + j * canal + 0]; // Azul

			bgrPixel.val[1] = pixelApt[i * imagen.cols * canal + j * canal + 1]; // Verde

			bgrPixel.val[2] = pixelApt[i * imagen.cols * canal + j * canal + 2]; // Rojo

			int ponderado = (bgrPixel.val[0]*0.114 + bgrPixel.val[1]*0.587 + bgrPixel.val[2]*0.299);

			array[i][j] = ponderado;
		}
	}
	Mat i_ntsc(Size(fila_original, columna_original), CV_8UC1, array, Mat::AUTO_STEP); // implementacion metodo promedidada
	// CV_8U1 : Es una matriz de un solo canal de 8 bits que se utiliza principalmente para almacenar y obtener los valores de cualquier imagen
	// Mat:: AUTO_STEP
	
	imshow("Gris Promedio", i_ntsc); // Se muestra la imagen en escala de grises metodo promediada

	/************************/
	waitKey(0); //Función para esperar
	return 1;
}
