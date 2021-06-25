/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mercado;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author
 */
public class Canasta 
{
    HashMap<String, Producto> productos = new HashMap();
    
    public void agregarProducto(Producto producto)
    {
        productos.put(producto.getSku(), producto);
    }
    
    public void eliminarProducto(String sku)
    {
        productos.remove(sku);
    }
    
    public void listaProductos()
    {
        int n=0;
        float total = 0;
        if(productos.isEmpty())
           System.out.println("\nCanasta vacía\n\n");
        else
        {
            System.out.println("Contenido de la canasta");
            System.out.println("==================================================================================");
            System.out.println("Np\tSKU\t        Descripcion\t\t               Precio");
            System.out.println("==================================================================================");
            for(Map.Entry <String, Producto> contenido : productos.entrySet()) // Recorrer 
            {
                Producto producto = contenido.getValue();
                total+=producto.getPrecio();
                n++;
                System.out.format("%d\t%s\t%s\t\t%.2f\n",n,producto.getSku(),producto.getDescripcion(),producto.getPrecio());
            }
            System.out.println("==================================================================================");
            System.out.format("El total es: $%.2f\n\n",total);
        }
    }
    
    public void vaciarCanasta()
    {
        productos.clear();
    }
}
