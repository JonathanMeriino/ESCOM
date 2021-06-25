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
public class Ejemplo01 {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Felino leon = new Felino("Simba","Felis Leo");
        leon.muestraInfo();
        leon.setNombre("Scar");
        leon.muestraInfo();
    }
    
}
