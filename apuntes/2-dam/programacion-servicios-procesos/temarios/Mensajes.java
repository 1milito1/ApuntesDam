package org.example;

public class Mensajes {
    // Define la cabecera HTTP para un respuesta existosa (código 200 ok)
    public static final String CABECERA_OK = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/html; charset=UTF-8\r\n" + "Conection: close\r\n\r\n";

    // Define la cabecera HTTP para una respeusta de error "Not Found" (Código 404)
    public static final String CABECERA_NOT_FOUND = "HTTP/1.1 404 Not Found\r\n" + "Content-Type: text/html; charset=UTF-8\r\n" + "Conection: close\r\n\r\n";
}
