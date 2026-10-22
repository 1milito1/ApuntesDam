package org.example;

import java.util.Random;

public class Paginas {

    // Array de curiosidades que se mostrarán aleatoriamente mediante un Random
    private static final String [] CURIOSIDADES = {
            "¿Sabías que la miel nunca se echa a perder?",
            "El corazón de una ballena azul es tan grande que una persona podría nadar por por sus arterias",
            "Los pulpos tienen tres corazones.",
            "Las huellas dactilares de los koalas son tan similares a las de los humanos que incluso lso expertos a veces tiene dificultades para distinguirlas",
            "El sonido más fuerte producido por un animal es el del camarón pistoal al cerrar su pinza"
    };

    private static final Random RANDOM = new Random(); //Creamos la instancia de Random para curiosidades aleatorias


    //Método para obtener la página de bienvenida
    public static String getPaginaBinevenida(){
        //Creación del documento HTML
        return "<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "<title>Bienvenido</title>\n" +
                "</head>\n" +
                "<h1>¡Bienvenido al Servidor de Curiosidades!</h1>\n" +
                "<p> Explora las curiosidades del mundo visitando <a href='/curiosidad'> /curiosidad</a>.</p>\n" +
                "<p>Contáctanos en <a href='/contacto'>/contacto</a>.</p>\n" +
                "</body>\n" +
                "</html>";
    }

    //Método para obtener la página de curiosidad
    public static String getPaginaCuriosidad() {
        int indice = RANDOM.nextInt(CURIOSIDADES.length); //Genera un indice aleatorio sobre el array de curiosidades
        return "<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "<title>Curiosidad</title>\n" +
                "</head>\n" +
                "<body>\n" +
                "<h1>Curiosidad del día</h1>\n" +
                "<p>" + CURIOSIDADES[indice] + "</p>\n" +
                "<p><a href='/'>Volver a la página principal</a></p>\n" +
                "</body>" +
                "</html>";
    }

    //Método para la página de contacto
    public static String getPaginaContacto() {
        return "<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "<title>Contacto</title>\n" +
                "</head>\n" +
                "<body>\n" +
                "<h1>Información de Contacto</h1>\n" +
                "<p>Email: info@curiosidadesdelmundo.com</p>\n" +
                "<p>Teléfono: +34 91 123 45 67</p>\n" +
                "<p>Dirección: Calle Ficticia, 123, Plasencia (España)</p>\n" +
                "<p><a href='/'>Volver a la página principal</a></p>\n" +
                "</body>\n" +
                "</html>";
    }

    //Método para obtener la página de error 404 (Not Found)
    public static String getPaginaNotFound() {
        return"<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                "<title>Error 404</title>\n" +
                "</head>\n" +
                "<body>\n" +
                "<h1>¡Error 404!</h1>\n" +
                "<p>La página solicitada no se ha encontrado.</p>\n" +
                "<p><a href='/'>Volver a la página principal</a></p>\n" +
                "</body>\n" +
                "</html>";
    }
}
