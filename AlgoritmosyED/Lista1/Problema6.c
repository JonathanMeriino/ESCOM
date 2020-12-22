/*Indique el estado de las cadenas antes y despues de invocar la funcion.
Codifique y/o complete las funciones que sean necesarias*/ 
#include <stdio.h>
#include<stdlib.h>
void main()
{
  char linea0[60]= “¿Encontraria a la Maga?”;
  char linea1[60]= “Andabamos sin buscarnos”;
  char linea2[60]= “pero sabiendo que andabamos para encontrarnos.”;
  char linea3[60]= “Rayuela, Julio Cortazar”;
  char rayuela= NULL;
  rayuela= crearArreglo(339);

  rayuela= concatenar(linea0, linea1);
  relatar(rayuela);

  rayuela= concatenar(linea1, linea2);
  relatar(rayuela);

  rayuela= concatenar(linea0, linea3);
  relatar(rayuela);
  redactar(rayuela,linea0);
  redactar(rayuela,linea1);
  redactar(rayuela,linea2);
  redactar(rayuela,linea3);

  relatar(rayuela);
  destruirArreglo(rayuela);
}
void relatar(char *cadena)
{
  int c=0;
    if (cadena==NULL)
      return;
    for (c=0; cadena[c]!=’0’; c++)
      printf(“%c”, cadena);
    printf(“\n”);
}
void concatenar(char *nuevo, char *prefijo, char *sufijo)
{
  int k=0, q=0;
  if (nuevo==NULL || prefijo==NULL || sufijo==NULL)
    return;
  for (k=0, q=0; prefijo[k]!=’\0’; k++, q++)
      nuevo[q]= prefijo[k];

  for (k=0; sufijo[k]!=’\0’; k++, q++)
      nuevo[q]= sufijo[k];
  nuevo[q]=’\0’;
}
void redactar(char *texto, char *cadena)
{
  int k=0, q=0;
  if (texto==NULL || cadena==NULL)
  return;

  for (q= 0; texto[q]!= ‘\0’; q++);

  for (k=0; cadena[k]!=’\0’; k++, q++)
      texto[q]= cadena[k];
  texto[q]=’\0’;
}
