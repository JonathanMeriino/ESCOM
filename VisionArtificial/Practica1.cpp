#include <opencv2/opencv.hpp>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
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
	Mat i_fun;
	Mat i_prom;
	Mat i_ntsc;
	/************************/

	/*********Lectura de la imagen*********/
	imagen = imread(NombreImagen);

	if (!imagen.data)
	{
		cout << "Error al cargar la imagen: " << NombreImagen << endl;
		exit(1);
	}
	/************************/

	/************Procesos*********/
	int fila_original = imagen.rows;
	int columna_original = imagen.cols;//Lectur de cuantas columnas
	uint8_t myArray[fila_original][columna_original];


	cout << "filas: " << fila_original << endl;
	cout << "columnas: " << columna_original << endl;

	namedWindow("Hola Mundo", WINDOW_AUTOSIZE);//Creación de una ventana
	imshow("Hola Mundo", imagen);
	
	/*Convertir la imagen de RGB a escala de grises (Funcion)*/

	cvtColor(imagen, i_fun, COLOR_BGR2GRAY);

	
	imshow("Escala de grises con funcion", i_fun);

	/*Convertir la imagen de RGB a escala de grises (Promedio)*/
	

	for (int i = 0; i < fila_original; i++) {
		for (int j = 0; j < columna_original; j++) {
			myArray[i][j] = 0;
		}
	}
	uint8_t* pixelPtr = (uint8_t*)imagen.data;

	int cn = imagen.channels();

	Scalar_<uint8_t> bgrPixel;

	for (int i = 0; i < fila_original; i++)

	{

		for (int j = 0; j < columna_original; j++)

		{

			bgrPixel.val[0] = pixelPtr[i * imagen.cols * cn + j * cn + 0]; // B

			bgrPixel.val[1] = pixelPtr[i * imagen.cols * cn + j * cn + 1]; // G

			bgrPixel.val[2] = pixelPtr[i * imagen.cols * cn + j * cn + 2]; // R

			int promedio = (bgrPixel.val[0] + bgrPixel.val[1] + bgrPixel.val[2]) / 3;

			myArray[i][j] = promedio;
		}
	}
	
	Mat i_prom(Size(fila_original, columna_original), CV_8UC1, myArray, Mat::AUTO_STEP);

	imshow("Gris Promedio", i_prom);
	/*Convertir la imagen de RGB a escala de grises (NTSC)*/



	/************************/

	waitKey(0); //Función para esperar
	return 1;
}