public class comic {
    public static void main(String[] args) {
        personaje alguien = new personaje("Heroe o antiheroe", "DC o Marvel","Bueno o malo","Mortal o docil");

        heroe mujer = new heroe("Mujer Maravilla","DC","Superfuerza","Lazo");
        heroe thor = new heroe("Thor","Marvel","Volador","Martillo");

        Antiheroe robin = new Antiheroe("Robin", "DC", "Liderazgo","Lazer");
        Antiheroe deadpool = new Antiheroe("Deadpool","Marvel","Agresivo","Espadas");

        alguien.showData();

        mujer.showData();
        mujer.luchar();
        mujer.entrenar();

        thor.showData();
        thor.luchar();
        thor.entrenar();

        robin.showData();
        robin.luchar();
        robin.entrenar();

        deadpool.showData();
        deadpool.luchar();
        deadpool.entrenar();

    }
}
