public class personaje {
    //Atributos
    private String nombre;
    private String universo;
    private String rasgoPersonalidad;
    private String arma;

    //constructor

    public personaje(String nombre, String universo, String rasgoPersonalidad, String arma) {
        this.nombre = nombre;
        this.universo = universo;
        this.rasgoPersonalidad = rasgoPersonalidad;
        this.arma = arma;
    }

    public String getNombre() {
        return nombre;
    }

    public String getUniverso() {
        return universo;
    }

    public String getRasgoPersonalidad() {
        return rasgoPersonalidad;
    }

    public String getArma() {
        return arma;
    }
    public void showData()
    {
        System.out.println("\nNombre personaje: "+nombre+
                            "\nUniverso: "+universo+
                             "\nRasgo personalidad: "+rasgoPersonalidad+
                                "\narma: "+arma);
    }
}
