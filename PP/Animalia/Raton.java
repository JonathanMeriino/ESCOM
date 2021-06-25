/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package animalia;

/**
 *
 * @author Macario
 */
public class Raton extends Mamifero implements Presa
{
    private String nombre;
    
    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }
    public String getNombre()
    {
        return nombre;
    }
    
    @Override
    public void sufrir()
    {
        System.out.println("Raton sufriendo");
    }
    
    @Override
    public void desplazarse()
    {
        System.out.println("Raton caminando");
    }
}
