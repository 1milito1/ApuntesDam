import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class OrdenarPalabras {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> palabras = new ArrayList<>();

        while (scanner.hasNextLine()) {
            String palabra = scanner.nextLine().trim();
            if (!palabra.isEmpty()) {
                palabras.add(palabra);
            }
        }

        Collections.sort(palabras);

        for (String palabra : palabras) {
            System.out.println(palabra);
        }

        scanner.close();
    }
}
