
public class autoridad extends persona implements contribuyente{
    //atributos
    private String cargo;
    private int años;

    //constructor
    public autoridad(String nombre,String apellido,int edad, String cargo, int años){
        super(nombre,apellido,edad);
        this.cargo = cargo;
        this.años = años;
    }

    //metodos
    public void mostrarDatos(){
        System.out.println("\nNombre autoridad: "+nombre+
                            "\nApellido autoridad: "+apellido+
                            "\nEdad autoridad: "+edad+
                            "\nCargo: "+cargo+
                            "\nAños: "+años);
    }
    public void paga(){
        System.out.println("La autoridad paga");
    }
    public void nopaga(){
        System.out.println("La autoridad no paga");
    }


}
