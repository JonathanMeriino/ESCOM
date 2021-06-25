
public class docente extends persona implements contribuyente
{
    //atributos
    private String materia;
    private int cedula;
    //constructor
    public docente(String nombre,String apellido,int edad,String materia,int cedula)
    {
        super(nombre,apellido,edad);
        this.materia = materia;
        this.cedula = cedula;
    }

    public void mostrarDatos()
    {
        System.out.println("\nNombre docente: "+nombre+
                            "\nApellido docente: "+apellido+
                            "\nEdad docente: "+edad+
                            "\nMateria: "+materia+
                            "\nCedula Profesional: "+cedula);
    }
    //metodo de contribuyente
    public void paga()
    {
        System.out.println("El docente paga");
    }
    public void nopaga()
    {
        System.out.println("El docente no paga");
    }
}
