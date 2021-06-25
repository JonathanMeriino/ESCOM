public class alumno extends persona implements aprendiz{
    //atributos
    private int boleta;
    private float promedio;

    public alumno(String nombre,String apellido, int edad, int boleta ,float promedio)
    {
        super(nombre,apellido,edad);
        this.boleta = boleta;
        this.promedio = promedio;

    }


    public void mostrarDatos()
    {
        System.out.println("\nNombre alumno: "+nombre+
                            "\nApellido alumno: "+apellido+
                            "\nEdad alumno: "+edad+
                            "\nBoleta: "+boleta+
                            "\nPromedio: "+promedio);
    }
    //metodos de aprendiz
    public void aprueba(){
        System.out.println("El alumno aprobo");

    }
    public void reprueba()
    {
        System.out.println("El alumno reprobo");
    }

}
