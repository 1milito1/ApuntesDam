public class Pedido {

	private int idPedido;
	private Socio socio;
	private ArrayList<Articulo> articulos;

	public int getIdPedido() {
		return this.idPedido;
	}

	public Socio getSocio() {
		return this.socio;
	}

	public ArrayList<Articulo> getArticulos() {
		return this.articulos;
	}

	public void agregarArticulos() {
		// TODO - implement Pedido.agregarArticulos
		throw new UnsupportedOperationException();
	}

	public double calcularTotal() {
		// TODO - implement Pedido.calcularTotal
		throw new UnsupportedOperationException();
	}

}