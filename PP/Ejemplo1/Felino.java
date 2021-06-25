/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejemplo01;

/**
 *
 * @author 
 */
public class Felino {
    
    private String nombre;
    private String especie;
    
    public Felino(String nombre, String especie)
    {
        this.nombre = nombre;
        this.especie = especie;
    }
    
    public void muestraInfo()
    {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Especie: " + this.especie);
    }

    public String getNombre()
    {
        return this.nombre;
    }
    
    public String getEspecie()
    {
        return this.especie;
    }   
    
    public void setNombre(String nombre)
    {
        if(nombre.length() > 0)
            this.nombre = nombre;
        else
            System.out.println("Asigne nombre no vacío");
    }
  
    public void setEspecie(String especie)
    {
        if(especie.length() > 0)
            this.especie = especie;
        else
            System.out.println("Asigne especie no vacía");
    }

}
