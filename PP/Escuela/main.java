public class main {
    public static void main(String[] args)
    {
        persona persona1 = new persona("Maritza","Aranda",18);
        alumno alumno1 = new alumno("Jonathan","Merino",17, 20201492,8.7f);
        docente docente1 = new docente("Macarario","Hernandez",30,"Paradigmas",17181919);
        autoridad autoridad1= new autoridad("Juan","Medina",45,"Director",3);

        persona1.caminar();
        persona1.mostrarDatos();

        alumno1.mostrarDatos();
        alumno1.aprueba();
        alumno1.reprueba();

        docente1.mostrarDatos();
        docente1.paga();
        docente1.nopaga();

        autoridad1.mostrarDatos();
        autoridad1.paga();
        autoridad1.nopaga();
    }

}
