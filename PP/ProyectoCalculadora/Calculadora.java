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
				case '+': memoria+=numero; break;
				case '-': memoria-=numero; break;
                case 'x': memoria*=numero; break;
                case '/': memoria/=numero;break;
                case 'I': memoria= Math.pow(numero,-1);break;

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
