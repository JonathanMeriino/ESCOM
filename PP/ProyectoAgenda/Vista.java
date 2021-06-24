
package proyectoagenda;

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

	private JLabel et1        = new JLabel("Nickname:");
	private JLabel et2        = new JLabel("Nombre:");
    private JLabel et3        = new JLabel("Email:");
    private JLabel et4       = new JLabel("Celular:");
    private JLabel et5      = new JLabel("Imagen:");
    private JLabel  imagen    = new JLabel();    

	private JTextField tNickname = new JTextField();
	private JTextField tNombre= new JTextField();
    private JTextField tEmail = new JTextField();
    private JTextField tCelular = new JTextField();
    private JTextField tImagen = new JTextField();
        
	private JButton    buscar  = new JButton("Buscar");
    private JButton    alta  = new JButton("Agregar");
    private JButton    borrar  = new JButton("Eliminar");
    private JButton    cambiar  = new JButton("Cambiar");
    private JButton    limpiar = new JButton("Limpiar");
        
        
	

	private Properties prop   = new Properties();  // Para guardar la conf de la base de datos

	// LA VISTA

	public Vista()
	{
		initComponents();
		this.setTitle("Agenda ESCOM");
		this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		this.setLayout(null);
		this.setBounds(10,10,600,350);
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
        et3.setBounds(10,110,100,30);
        et4.setBounds(10,150,100,30);
        et5.setBounds(10,190,100,30);
            
            
	    imagen.setBounds(400,30,125,170);
            
	    tNickname.setBounds(80,30,100,30);
	    tNombre.setBounds(80,70,300,30);
        tEmail.setBounds(80,110,300,30);
        tCelular.setBounds(80,150,300,30);
        tImagen.setBounds(80,190,300,30);
          
        buscar.setBounds(310,30,80,30);
            
        alta.setBounds(110,230,80,30);
        borrar.setBounds(210,230,80,30);
        cambiar.setBounds(310,230,85,30);
        limpiar.setBounds(10,230,80,30);
            
            
	    add(et1);
	    add(et2);
        add(et3);
        add(et4);
        add(et5);
	    
		add(tNickname);
	    add(tNombre);
        add(tEmail);
        add(tCelular);
        add(tImagen);
	    
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
			if(tNickname.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura nickname, no lo puedes dejar vacio", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
				Persona newPersona = Persona.getLibroFromDB(tNickname.getText(),prop); // Invoca al Modelo
				if(newPersona != null)
				{
					tNombre.setText(newPersona.getnombre());
                	tEmail.setText(newPersona.getEmail());
                    tCelular.setText(newPersona.getCelular());
                    tImagen.setText(newPersona.getImagen1());
					String nombreArchivoImagen = newPersona.getImagen();
					imagen.setIcon(new ImageIcon(nombreArchivoImagen));
				}
				else
				JOptionPane.showMessageDialog(this, "No existe la persona", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);

			}
		}

		if(fuenteDelEvento == cambiar)
		{
			// Hacer algo
			if(tNickname.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura nickname, no lo puedes dejar vacio", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
				Persona newPersona = Persona.getPersonaFromDB(tNickname.getText(),prop); // Invoca al Modelo
                              
                if(newPersona != null)
				{		
                    newPersona.setNombre(tNombre.getText());
                    newPersona.setEmail(tEmail.getText());
                    newPersona.setCelular(tCelular.getText());
                    newPersona.setImagen(tImagen.getText());
                        // Actualiza el titulo del objeto libro
                                    
                        if(newBook.cambiar(prop)) // Si hubo éxito
                            JOptionPane.showMessageDialog(this, "Registro actualizado: " + tNickname.getText(), "Aviso!",JOptionPane.INFORMATION_MESSAGE);
                        else
                            JOptionPane.showMessageDialog(this, "Acción no realizada!!","Aviso!",JOptionPane.ERROR_MESSAGE);
        			}
				else
				JOptionPane.showMessageDialog(this, "No existe la persona", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);

			}
		}

                if(fuenteDelEvento == alta)
		{
			// Hacer algo
			if(tNickname.getText().length() == 0)
			{
				JOptionPane.showMessageDialog(this, "Captura Nickname, no lo puedes dejar vacio", "Aviso!",
							                          JOptionPane.ERROR_MESSAGE);
			}
			else
			{
                // Creamos una nueva persona con los datos de la vista
                                
                    Persona newPersona = new Persona();
                    newPersona.setNickname(tNickname.getText());
                    newPersona.setNombre(tNombre.getText());
                    newPersona.setEmail(tEmail.getText());
                    newPersona.setCelular(tCelular.getText());
                    newPersona.setImagen(tImagen.getText());
                                
                    // Se ejecuta el alta
                                
                    if(newBook.alta(prop)) // Si la alta fue exitosa
                        JOptionPane.showMessageDialog(this, "Registro agregado: " + tNickname.getText(), "Aviso!",JOptionPane.INFORMATION_MESSAGE);
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
				if(tNickname.getText().length() == 0)
				{
					JOptionPane.showMessageDialog(this, "Captura Nickname, no lo puedes dejar vacio", "Aviso!",JOptionPane.ERROR_MESSAGE);
				}
				else
				{
					Libro newBook = Libro.getLibroFromDB(tNickname.getText(),prop); // Invoca al Modelo
					if(newBook != null)
					{
                                    if(newBook.borrar(prop)) // Si hubo éxito
                                    {   
                                        JOptionPane.showMessageDialog(this, "Registro eliminado: " + tNickname.getText(), "Aviso!",JOptionPane.WARNING_MESSAGE);
                                        limpiarCampos();
                                    }    
                                   else JOptionPane.showMessageDialog(this, "Acción no realizada!!","Aviso!",JOptionPane.ERROR_MESSAGE);
                           
					}
					else
						JOptionPane.showMessageDialog(this, "No existe la persona", "Aviso!",JOptionPane.ERROR_MESSAGE);

				}
            }
		}
                
 	}
        
        private void limpiarCampos()
        {
            tNickname.setText("");
            tNombre.setText("");
            tEmail.setText("");
            tCelular.setText("");
            tImagen.setText("");
			imagen.setIcon(null);
        }

}
