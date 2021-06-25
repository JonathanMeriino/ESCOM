/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pruebajdbc;

import java.sql.*;
import javax.swing.*;

/**
 *
 * @author Macario
 */
public class PruebaJDBC {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        String mySQLHost = "jdbc:mysql://localhost:3306/";
        String dbName = "world";
        String user = "root";
        String password = "";
        JPasswordField pwd = new JPasswordField(10);
        int option = JOptionPane.showConfirmDialog(null, pwd,"Enter root password",JOptionPane.OK_CANCEL_OPTION);
        if(option==0) password = new String(pwd.getPassword());
         
        Connection con=null;
	try
	{
            Class.forName("com.mysql.cj.jdbc.Driver");   //Carga el driver
            String urlBD = mySQLHost + dbName+ "?user=" + user + "&password=" + password + "&useSSL=false";
            con = DriverManager.getConnection(urlBD);
            Statement st = con.createStatement();
            if(st.execute("show databases"))
            {
                String resultados = "";
                ResultSet rs = st.getResultSet();
                while(rs.next())
                {
                    resultados+=rs.getString(1)+"\n";
                }
                JOptionPane.showMessageDialog(null, resultados, "Éxito!!! Esta es la lista de bases de datos:", JOptionPane.INFORMATION_MESSAGE);
            }
            con.close();
        }
	catch (ClassNotFoundException ex)
        {
           
            String javaHome = System.getProperty("java.home");
            System.out.println("No encuentro el Driver, debe estar en un archivo .JAR)");
            System.out.println("Ponga el JAR del Driver de MySQL en la carpeta : \n" + javaHome + "\\lib\\ext \ndel Equipo Host");
            JOptionPane.showConfirmDialog(null,"Ponga el jar del Driver de MySQL en la carpeta : \n" + javaHome + "\\lib\\ext \ndel Equipo Host" , "Problema!!!" ,JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
            ex.printStackTrace();
	}
        catch (SQLException ex)
        {
            JOptionPane.showConfirmDialog(null, "Error al hacer la conexión o la consulta", "Problema!!!" ,JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
            ex.printStackTrace();
        }
    }
    
}
