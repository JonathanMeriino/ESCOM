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
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.io.*;

public class Vista extends JFrame implements ActionListener
{

	private boolean nuevo=true;

	private JMenuBar barraMenus = new JMenuBar();

	private JMenu archivo 	  = new JMenu("Archivo");
	private JMenuItem salir   = new JMenuItem("Salir");

	private JLabel et1        = new JLabel("ISNB:");
	private JLabel et2        = new JLabel("Libro:");
	private JTextField tIsbn  = new JTextField();
	private JTextField tTitulo= new JTextField();
	private JButton    buscar  = new JButton("Buscar");
        private JButton    alta  = new JButton("Agregar");
        private JButton    borrar  = new JButton("Eliminar");
        private JButton    cambiar  = new JButton("Cambiar");
        private JButton    limpiar = new JButton("Limpiar");
        
        
	private JLabel  imagen    = new JLabel();

	private Properties prop   = new Properties();  // Para guardar la conf de la base de datos

	// LA VISTA

	public Vista()
	{
		initComponents();
		this.setTitle("Libreria El Zangano (CRUD)");
		this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		this.setLayout(null);
		this.setBounds(10,10,600,300);
		this.setJMenuBar(barraMenus);

                // Carga las propiedades desde el archivo
		try
		{
			prop.load(new FileInputStream("config.properties"));
		}
		catch (Exception ex)
		{
			ex.printStackTrace();
		}

		this.setVisible(true);

	}


	public void initComponents()
	{
            // Diseña el menu

            barraMenus.add(archivo);
            archivo.add(salir);

		// Componentes

	    et1.setBounds(10,30,100,30);
	    et2.setBounds(10,70,100,30);
	    imagen.setBounds(400,30,125,170);
	    tIsbn.setBounds(80,30,100,30);
	    tTitulo.setBounds(80,70,300,30);
	    buscar.setBounds(310,30,80,30);
            alta.setBounds(110,120,80,30);
            borrar.setBounds(210,120,80,30);
            cambiar.setBounds(310,120,85,30);
            limpiar.setBounds(10,120,80,30);
            
            
	    add(et1);
	    add(et2);
	    add(tIsbn);
	    add(tTitulo);
	    add(buscar);
            add(alta);
            add(borrar);
            add(cambiar);
            add(limpiar);
	    add(imagen);


            salir.addActionListener(this);
            buscar.addActionListener(this);
            limpiar.addActionListener(this);
            borrar.addActionListener(this);
            alta.addActionListener(this);
            cambiar.addActionListener(this);
            
            
            
            class MyWindowAdapter extends WindowAdapter
            {
		public void windowClosing(WindowEvent e)
		{
			System.exit(0);
		}
            }
            addWindowListener(new MyWindowAdapter());   

	}


	// EL CONTROLADOR (GESTIONA LOS EVENTOS)

	public void actionPerformed(ActionEvent objetoEvento)
	{
		Object fuenteDelEvento = objetoEvento.getSource();

		// Identifica sobre qué objeto generó el evento

		if(fuenteDelEvento == salir) System.exit(0);  // Cierra el Programa

                if(fuenteDelEvento == limpiar) limpiarCampos();

                
		if(fuenteDelEvento == buscar)
		{
			// Hacer algo
			if(tIsbn.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura ISBN, no lo puedes dejar en blanco", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
				Libro newBook = Libro.getLibroFromDB(tIsbn.getText(),prop); // Invoca al Modelo
				if(newBook != null)
				{
					tTitulo.setText(newBook.getTitulo());
					String nombreArchivoImagen = newBook.getImagen();
					imagen.setIcon(new ImageIcon(nombreArchivoImagen));
				}
				else
				JOptionPane.showMessageDialog(this, "No existe el libro", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);

			}
		}

		if(fuenteDelEvento == cambiar)
		{
			// Hacer algo
			if(tIsbn.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura ISBN, no lo puedes dejar en blanco", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
				Libro newBook = Libro.getLibroFromDB(tIsbn.getText(),prop); // Invoca al Modelo
                              
                                if(newBook != null)
				{
                                    newBook.setTitulo(tTitulo.getText()); // Actualiza el titulo del objeto libro
                                    
                                    if(newBook.cambiar(prop)) // Si hubo éxito
                                      JOptionPane.showMessageDialog(this, "Registro actualizado: " + tIsbn.getText(), "Aviso!",JOptionPane.INFORMATION_MESSAGE);
                                    else
                                       JOptionPane.showMessageDialog(this, "Acción no realizada!!","Aviso!",JOptionPane.ERROR_MESSAGE);
        			}
				else
				JOptionPane.showMessageDialog(this, "No existe el libro", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);

			}
		}

                if(fuenteDelEvento == alta)
		{
			// Hacer algo
			if(tIsbn.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura ISBN, no lo puedes dejar en blanco", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
                                // Creamos un nuevo libro con los datos de la vista
                                
                                Libro newBook = new Libro();
                                newBook.setIsbn(tIsbn.getText());
                                newBook.setTitulo(tTitulo.getText());
                                
                                // Y ejecutamos la alta
                                
                                if(newBook.alta(prop)) // Si la alta fue exitosa
                                   JOptionPane.showMessageDialog(this, "Registro agregado: " + tIsbn.getText(), "Aviso!",JOptionPane.INFORMATION_MESSAGE);
                                else
                                   JOptionPane.showMessageDialog(this, "Acción no realizada!!","Aviso!",JOptionPane.ERROR_MESSAGE);
                           
			}
		}
                
		if(fuenteDelEvento == borrar)
		{
                    
                    int respuesta = JOptionPane.showConfirmDialog(this, "Desea borrar este registro?", "Atención!!!", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
                    
                    if(respuesta==JOptionPane.YES_OPTION) // Si el usuario está seguro
                    {
			// Hacer algo
			if(tIsbn.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura ISBN, no lo puedes dejar en blanco", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
				Libro newBook = Libro.getLibroFromDB(tIsbn.getText(),prop); // Invoca al Modelo
				if(newBook != null)
				{
                                    if(newBook.borrar(prop)) // Si hubo éxito
                                    {   
                                        JOptionPane.showMessageDialog(this, "Registro eliminado: " + tIsbn.getText(), "Aviso!",JOptionPane.WARNING_MESSAGE);
                                        limpiarCampos();
                                    }    
                                   else JOptionPane.showMessageDialog(this, "Acción no realizada!!","Aviso!",JOptionPane.ERROR_MESSAGE);
                           
				}
				else
				JOptionPane.showMessageDialog(this, "No existe el libro", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);

			}
                    }
		}
                
 	}
        
        private void limpiarCampos()
        {
                    tIsbn.setText("");
                    tTitulo.setText("");
                    imagen.setIcon(null);
        }

}
