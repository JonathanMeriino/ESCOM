/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mercado;

/**
 *
 * @author 
 */
public class Producto 
{
    String sku = new String();
    String descripcion = new String();
    float precio;
    
    public Producto(String sku, String descripcion, float precio)
    {
        this.sku = sku;
        this.descripcion = descripcion;
        this.precio = precio;
    }
    
    public void setSku(String sku)
    {
        this.sku = sku;
    }
 
    public void setDescripcion(String descripcion)
    {
        this.descripcion = descripcion;
    }
    
    public void setPrecio(float precio)
    {
        this.precio = precio;
    }
    
    public String getSku()
    {
        return sku;
    }
    
    public String getDescripcion()
    {
        return descripcion;
    }
    
    public float getPrecio()
    {
        return precio;
    }
}
