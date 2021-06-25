/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectocalculadora;

/**
 *
 * @author Macario
 */
public class Calculadora 
{
        private double memoria=0;
	    private char ultimoOperador='=';
        private boolean radianes=true;


	public void operacion(double numero, char operador)
	{
		if(ultimoOperador=='=')
		  memoria = numero;
		else
			switch(ultimoOperador)
			{
				case '+': memoria+=numero; break; // suma
				case '-': memoria-=numero; break; // resta
                case '*': memoria*=numero;break; // multiplicacion
                case '/': memoria/=numero;break; // division

                case 'x': memoria=Math.pow(memoria,numero); break; // potencia
                case 'A': memoria=Math.sqrt(numero); break; // calcula la raiz cuadrada
                case 'B': memoria =Math.cbrt(numero);break; // calcula la raiz cibica
                case 'P': memoria=Math.PI;break; // imprimer el valor de PI
                case 'e': memoria=Math.E; break; // imprimir el valor de euler

                case 'S':
                    memoria=Math.sin(numero*(Math.PI/180));break; // calcula el seno
                case 'C':
                    memoria=Math.cos(numero*(Math.PI/180));break; // calcula el coseno
                case 'T':
                    memoria=Math.tan(numero*(Math.PI/180));break; // calcula la tangente
                case 'I': memoria=1/memoria;break; // calcula el inverso del numero

			}
		     ultimoOperador=operador;
	}

        public void clearMemory()
        {
            memoria=0;
        }
        
	public double getMemoria()
	{
		return memoria;
	}

        public void setRadianes()
        {
            radianes=false;
        }
        
        public void setDegrees()
        {
            radianes=false;
        }
        
        public boolean isRadianes()
        {
            return radianes;
        }
}
