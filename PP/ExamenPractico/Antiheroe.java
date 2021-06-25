public class Antiheroe extends personaje implements Peleador{

    public Antiheroe(String nombre, String universo, String rasgoPersonalidad, String arma) {
        super(nombre, universo, rasgoPersonalidad, arma);
    }
    public void showData()
    {
        System.out.println("\nNombre antiheroe: "+getNombre()+
                "\nUniverso antiheroe: "+getUniverso()+
                "\nRasgo Personalidad antiheroe: "+getRasgoPersonalidad()+
                "\nArma antiheroe: "+getArma());
    }
    public void entrenar()
    {
        System.out.println("El antiheroe esta entrenando");
    }
    public void luchar()
    {
        System.out.println("El antiheroe esta luchando");
    }

}
