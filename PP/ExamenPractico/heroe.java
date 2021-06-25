public class heroe extends personaje implements Peleador{

    public heroe(String nombre, String universo, String rasgoPersonalidad, String arma) {
        super(nombre, universo, rasgoPersonalidad, arma);
    }

    public void showData()
    {
        System.out.println("\nNombre heroe: "+getNombre()+
                            "\nUniverso Heroe: "+getUniverso()+
                            "\nRasgo Personalidad: "+getRasgoPersonalidad()+
                            "\nArma: "+getArma());
    }

    public void entrenar()
    {
        System.out.println("El heroe esta entrenando");
    }
    public void luchar()
    {
        System.out.println("El antiheroe esta luchando");
    }

}
