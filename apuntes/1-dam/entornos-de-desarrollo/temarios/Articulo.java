public class Articulo {

	private String nombre;
	private double precio;
	private String descripcion;
	private int cantidadStock;

	public String getNombre() {
		return this.nombre;
	}

	public double getPrecio() {
		return this.precio;
	}

	public String getDescripcion() {
		return this.descripcion;
	}

	public int getCantidadStock() {
		return this.cantidadStock;
	}

	public void reducirStock() {
		// TODO - implement Articulo.reducirStock
		throw new UnsupportedOperationException();
	}

}