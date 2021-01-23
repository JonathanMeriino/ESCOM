#include <stdio.h>
#include <stdlib.h>

#define XSIZE 8
#define YSIZE 8
int tablero[YSIZE][XSIZE] = { {0} };

int desplazamiento[8][2] = {
  { -2,  1 }, { -1,  2 }, {  1,  2 }, {  2,  1 },
  {  2, -1 }, {  1, -2 }, { -1, -2 }, { -2, -1 }
};

void imprimir_tablero ();
int validar (int x, int y);
int sol_tablero (int x, int y, int n);
int compar (const void *a, const void *b);

int main ()
{
  if (sol_tablero (0, 0, 1))
    imprimir_tablero ();
  else
    printf ("No hay solucion.\n");
  return 0;
}

void imprimir_tablero ()
{
  int x, y;
  for (y = 0; y < YSIZE; y++)
    {
      for (x = 0; x < XSIZE; x++)
	printf ("% 6d ", tablero[y][x]);
      printf ("\n");
    }
}

int validar (int x, int y)
{
  return
    x >= 0 && x < XSIZE &&
    y >= 0 && y < YSIZE &&
    tablero[y][x] == 0;
}

int compar (const void *a, const void *b)
{
  return ((int *) a)[0] - ((int *) b)[0];
}

int sol_tablero (int x, int y, int n)
{
  tablero[y][x] = n;
  if (n == XSIZE * YSIZE)
    return 1;

  /* Gather valid moves and count their "loneliness". */
  int i, j, validos[8][3];
  for (i = 0; i < 8; i++)
    {
      validos[i][0] = 0;
      validos[i][1] = x + desplazamiento[i][0];
      validos[i][2] = y + desplazamiento[i][1];
      if (validar (validos[i][1], validos[i][2]))
	for (j = 0; j < 8; j++)
	  if (validar (validos[i][1] + desplazamiento[j][0],
		     validos[i][2] + desplazamiento[j][1]))
	    validos[i][0]++;
    }

  /* Sort and try each one. */
 qsort (&validos[0][0], 8, 3 * sizeof (int), &compar);
  for (i = 0; i < 8; i++)
    if (validar (validos[i][1], validos[i][2]) &&
	sol_tablero (validos[i][1], validos[i][2], n + 1))
      return 1;

  /* Dead end: back off. */
  tablero[y][x] = 0;
  return 0;
}