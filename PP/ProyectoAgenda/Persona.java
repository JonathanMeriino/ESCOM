/
package proyectolibreria;


import java.sql.*;
import java.util.*;

public class Persona
{
	private String Nickname;
	private String Nombre;
	
	private String imagen;
        private String Email;
        private String Celular;
       
	

	public Persona()
	{}

	public Persona(String nickname, String nombre,  String imagen, double precio,String Email,String Celular)
	{
		this.Nickname = nickname;
		this.Nombre= nombre;
		this.imagen = imagen;
                this.Email = Email;
                 this.Celular = Celular;

	}

	// Metodos get

	
public String getNickname()
	{
		return Nickname;
	}
public String getnombre()
	{
		return Nombre;
	}


        
        public String getEmail()
	{
		return Email;
	}
        public String getCelular()
	{
		return Celular;
	}


	public String getImagen()
	{
		return "imagenes/" + imagen +".jpg";
	}
        
        public String getImagen1()
	{
		return imagen;
	}



	// Métodos set

	public void setNombre(String nombre)
	{
		this.Nombre = nombre;
	}

	public void setNickname(String nickname)
	{
		this.Nickname = nickname;
	}

	
        public void setEmail(String Email)
	{
		this.Email = Email;
	}
         public void setCelular(String Celular)
	{
		this.Celular = Celular;
	}

	public void setImagen(String imagen)
	{
		this.imagen = imagen;
	}




	public void muestraDatos()
	{
		System.out.println("Nickname  :" + Nickname);
		System.out.println("Nombre:" + Nombre);
                System.out.println("Email :" + Email);
                System.out.println("Celular :" + Celular);
                System.out.println("imagen :" + imagen);
	}


	public static Persona getPersonaFromDB(String NicknameConsulta, Properties prop)
	{
            Persona persona = new Persona(); // Nuevo libro en blanco

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

                PreparedStatement ps = con.prepareStatement("SELECT * FROM agenda WHERE Nickname = ?");
                ps.setString(1,NicknameConsulta);
                boolean ok = ps.execute();
                ResultSet rs = ps.getResultSet();

                if(rs!=null && rs.next())
                {
                    String Nickname  = rs.getString("Nickname");
                    String Nombre = rs.getString("Nombre");
                    String imagen = rs.getString("imagen");
                    String Email = rs.getString("Email");
                    String Celular = rs.getString("Celular");
                    

                    persona.setNickname(Nickname);
                    persona.setNombre(Nombre);
                    persona.setImagen(imagen);
                    persona.setEmail(Email);
                    persona.setCelular(Celular);
                    con.close();
                    return persona;
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

                PreparedStatement ps = con.prepareStatement("UPDATE agenda SET Nombre = ?,Email = ?,Celular = ? ,imagen = ? WHERE Nickname = ?");
                
                ps.setString(1, this.Nombre); // El titulo que llega de la Vista
                ps.setString(2, this.Email);
                ps.setString(3, this.Celular);
                ps.setString(4, this.imagen);
                ps.setString(5, this.Nickname);
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

                PreparedStatement ps = con.prepareStatement("DELETE FROM agenda WHERE Nickname = ?");
                ps.setString(1, this.Nickname);
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

                PreparedStatement ps = con.prepareStatement("INSERT INTO agenda (Nickname, Nombre,Email,Celular,imagen) VALUES (?,?,?,?,?)");
                ps.setString(1, this.Nickname); 
                ps.setString(2, this.Nombre); 
                ps.setString(3, this.Email); 
                ps.setString(4, this.Celular); 
                 ps.setString(5, this.imagen); 
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