import java.util.Random;

public class GenerarPalabras {
    public static void main(String[] args) {
        Random random = new Random();
        int totalPalabras = 30;

        for (int i = 0; i < totalPalabras; i++) {
            int longitud = 3 + random.nextInt(6);
            StringBuilder palabra = new StringBuilder();

            for (int j = 0; j < longitud; j++) {
                char letra = (char) ('a' + random.nextInt(26));
                palabra.append(letra);
            }

            System.out.println(palabra);
        }
    }
}
