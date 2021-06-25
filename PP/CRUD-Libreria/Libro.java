/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectolibreria;

/**
 *
 * @author Macario
 */

import java.sql.*;
import java.util.*;

public class Libro
{
	private String isbn;
	private String titulo;
	private String autor;
	private String imagen;
	private double precio;

	public Libro()
	{}

	public Libro(String isbn, String titulo, String autor, String imagen, double precio)
	{
		this.isbn = isbn;
		this.titulo = titulo;
		this.autor = autor;
		this.imagen = imagen;
		this.precio = precio;

	}

	// Metodos get

	public String getIsbn()
	{
		return isbn;
	}

	public String getTitulo()
	{
		return titulo;
	}

	public String getAutor()
	{
		return autor;
	}

	public String getImagen()
	{
		return "imagenes/" + imagen;
	}

	public  double getPrecio()
	{
		return precio;
	}

	// Métodos set

	public void setIsbn(String isbn)
	{
		this.isbn = isbn;
	}

	public void setTitulo(String titulo)
	{
		this.titulo = titulo;
	}

	public void setAutor(String autor)
	{
		this.autor = autor;
	}

	public void setImagen(String imagen)
	{
		this.imagen = imagen;
	}

	public void setPrecio(double precio)
	{
		this.precio = precio;
	}


	public void muestraDatos()
	{
		System.out.println("ISBN  :" + isbn);
		System.out.println("Titulo:" + titulo);
		System.out.println("Autor :" + autor);
		System.out.println("Precio:" + precio);
	}


	public static Libro getLibroFromDB(String isbnConsulta, Properties prop)
	{
            Libro libro = new Libro(); // Nuevo libro en blanco

            try
	    {

                String driver = prop.getProperty("dbdriver");
                String host   = prop.getProperty("dbhost");
                String user   = prop.getProperty("dbuser");
                String password = prop.getProperty("dbpassword");
                String name     = prop.getProperty("dbname");
                String url = host + name  + "?user=" + user + "&password=" + password + "&useSSL=false";
                System.out.println("Conexion a la BD: " + url);


                Class.forName(driver);     // Carga el driver


                Connection con = DriverManager.getConnection(url); // Crea una conexion a la BD

                PreparedStatement ps = con.prepareStatement("SELECT * FROM LIBRO WHERE ISBN = ?");
                ps.setString(1,isbnConsulta);
                boolean ok = ps.execute();
                ResultSet rs = ps.getResultSet();

                if(rs!=null && rs.next())
                {
                    String isbn   = rs.getString("isbn");
                    String titulo = rs.getString("titulo");
                    String autor  = rs.getString("autor");
                    String imagen = rs.getString("imagen");
                    double precio = rs.getDouble("precio");

                    libro.setIsbn(isbn);
                    libro.setTitulo(titulo);
                    libro.setAutor(autor);
                    libro.setImagen(imagen);
                    libro.setPrecio(precio);
                    con.close();
                    return libro;
                }

	    }
	    catch (Exception ex)
	    {
	    	ex.printStackTrace();
	    }
	    return null;
	}
        
        public boolean cambiar(Properties prop)
	{
            boolean exito = false;
            
            try
	    {

                String driver = prop.getProperty("dbdriver");
                String host   = prop.getProperty("dbhost");
                String user   = prop.getProperty("dbuser");
                String password = prop.getProperty("dbpassword");
                String name     = prop.getProperty("dbname");
                String url = host + name  + "?user=" + user + "&password=" + password;
                System.out.println("Conexion a la BD: " + url);


                Class.forName(driver);     // Carga el driver


                Connection con = DriverManager.getConnection(url); // Crea una conexion a la BD

                PreparedStatement ps = con.prepareStatement("UPDATE LIBRO SET TITULO = ? WHERE ISBN = ?");
                
                ps.setString(1, this.titulo); // El titulo que llega de la Vista
                ps.setString(2, this.isbn);
                exito = ps.executeUpdate() > 0;
                con.close();
               
	    }
	    catch (Exception ex)
	    {
	    	ex.printStackTrace();
	    }
	    return exito;
	}

        public boolean borrar(Properties prop)
	{
            boolean exito = false;
            
            try
	    {

                String driver = prop.getProperty("dbdriver");
                String host   = prop.getProperty("dbhost");
                String user   = prop.getProperty("dbuser");
                String password = prop.getProperty("dbpassword");
                String name     = prop.getProperty("dbname");
                String url = host + name  + "?user=" + user + "&password=" + password;
                System.out.println("Conexion a la BD: " + url);


                Class.forName(driver);     // Carga el driver


                Connection con = DriverManager.getConnection(url); // Crea una conexion a la BD

                PreparedStatement ps = con.prepareStatement("DELETE FROM LIBRO WHERE ISBN = ?");
                ps.setString(1, this.isbn);
                exito = ps.executeUpdate() > 0;
                con.close();
               
	    }
	    catch (Exception ex)
	    {
	    	ex.printStackTrace();
	    }
	    return exito;
	}

        public boolean alta(Properties prop)
	{
            boolean exito = false;
            
            try
	    {

                String driver = prop.getProperty("dbdriver");
                String host   = prop.getProperty("dbhost");
                String user   = prop.getProperty("dbuser");
                String password = prop.getProperty("dbpassword");
                String name     = prop.getProperty("dbname");
                String url = host + name  + "?user=" + user + "&password=" + password;
                System.out.println("Conexion a la BD: " + url);


                Class.forName(driver);     // Carga el driver


                Connection con = DriverManager.getConnection(url); // Crea una conexion a la BD

                PreparedStatement ps = con.prepareStatement("INSERT INTO LIBRO (ISBN, TITULO) VALUES (?,?)");
                ps.setString(1, this.isbn); 
                ps.setString(2, this.titulo); 
                exito = ps.executeUpdate() > 0;
                con.close();
               
	    }
	    catch (Exception ex)
	    {
	    	ex.printStackTrace();
	    }
	    return exito;
	}

        
}