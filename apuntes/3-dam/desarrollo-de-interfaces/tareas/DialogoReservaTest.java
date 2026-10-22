package tarea1padelapp;


import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*; 
import static org.mockito.Mockito.*;
import javax.swing.SwingUtilities;

public class DialogoReservaTest {

    private DialogoReserva dialog;
    private GestionBBDD mockBBDD;

    @Before 
    public void setUp() throws Exception {
       
        java.awt.EventQueue.invokeAndWait(() -> {
            dialog = new DialogoReserva(new javax.swing.JFrame(), true);
            mockBBDD = mock(GestionBBDD.class);
            dialog.gestionBBDD = mockBBDD;
        });
    }

    @Test
    public void testFlujoReserva() throws Exception {
        java.awt.EventQueue.invokeAndWait(() -> {

            dialog.getTxtNombre().setText("Emilio Padel");
            dialog.getTxtTlf().setText("666777888");
            

            dialog.getBtnEnviar().doClick();


            verify(mockBBDD).guardarReservas("Emilio Padel", "666777888");
        });
    }
}