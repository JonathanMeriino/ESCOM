

public class persona {
    //Atributos
    protected String nombre;
    protected String apellido;
    protected int edad;
    //constructor


    public persona(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    //metodo clase persona
    public void caminar(){
        System.out.println("Una persona camina");
    }

    public void mostrarDatos(){
        System.out.println("\nNombre persona: "+nombre+
                            "\nApellido persona: "+apellido+
                            "\nEdad persona: "+edad);
    }
}
