/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectocalculadora;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

/**
 *
 * @author Macario
 */
public class Vista extends JFrame implements ActionListener
{
        // El objeto calculadora es el que realmente realiza las operaciones
    	private Calculadora casio = new Calculadora();
    	private boolean nuevo=true;

	private JMenuBar barraMenus = new JMenuBar();

	private JMenu archivo 	  = new JMenu("Archivo");
	private JMenuItem salir   = new JMenuItem("Salir");

	private JTextField display = new JTextField();
        private JButton b0 = new JButton("0");
	private JButton b1 = new JButton("1");
	private JButton b2 = new JButton("2");
	private JButton b3 = new JButton("3");
	private JButton b4 = new JButton("4");
	private JButton b5 = new JButton("5");
	private JButton b6 = new JButton("6");
	private JButton b7 = new JButton("7");
	private JButton b8 = new JButton("8");
	private JButton b9 = new JButton("9");
	private JButton mas= new JButton("+");
	private JButton menos=new JButton("-");
	private JButton igual=new JButton("=");
	private JButton cE   = new JButton("CE");
	private JButton multiplicacion = new JButton("*");
	private JButton division = new JButton("/");
	private JButton inverso = new JButton("I");
	private JButton potencia2 = new JButton("x²");
	private JButton raizCuadrada = new JButton("raiz²");
	private JButton raizCubica = new JButton("raiz³");
	private JButton seno = new JButton("S");
	private JButton coseno = new JButton("cos");
	private JButton tangente = new JButton("tan");
	private JButton e = new JButton("e");
	private JButton pi = new JButton("PI");

	public Vista()
	{
		initComponents();
		this.setTitle("Calculadora");
		this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
		this.setLayout(null); // Se deshabilita el Gestor de Distribución
		this.setBounds(100,100,520,400);
		this.setJMenuBar(barraMenus);
		this.setVisible(true);

	}

	public void initComponents()
	{
		// Diseña el menu

		barraMenus.add(archivo);
		archivo.add(salir);

		// Al desabilitar el LayoutManager, el programador tiene
		// la responsabilidad de situar los componentes

		display.setBounds(10,5,480,40);

		inverso.setBounds(10,50,50,50);
		potencia2.setBounds(70,50,50,50);
		raizCuadrada.setBounds(130,50,60,50);
		seno.setBounds(10,110,55,50);
		coseno.setBounds(70,110,55,50);
		tangente.setBounds(130,110,55,50);
		raizCubica.setBounds(130,170,60,50);
		e.setBounds(70,170,50,50);
		pi.setBounds(10,170,50,50);
		multiplicacion.setBounds(380,170,50,50);
		division.setBounds(440,170,50,50);



		b1.setBounds(200,50,50,50);
		b2.setBounds(260,50,50,50);
		b3.setBounds(320,50,50,50);
		b4.setBounds(200,110,50,50);
		b5.setBounds(260,110,50,50);
		b6.setBounds(320,110,50,50);
		b7.setBounds(200,170,50,50);
		b8.setBounds(260,170,50,50);
		b9.setBounds(320,170,50,50);
		b0.setBounds(260,230,50,50);
		cE.setBounds(380,50,50,50);
		igual.setBounds(440,50,50,50);
		mas.setBounds(380,110,50,50);
		menos.setBounds(440,110,50,50);
		multiplicacion.setBounds(380,170,50,50);
		division.setBounds(440,170,50,50);


		display.setBackground(Color.black);
		display.setForeground(Color.orange);
		display.setFont(new Font("Consolas",Font.BOLD, 26));
		display.setHorizontalAlignment(JTextField.RIGHT);
		display.setEditable(false);

		this.add(display);

		this.add(b1);
		this.add(b2);
		this.add(b3);
		this.add(b4);
		this.add(b5);
		this.add(b6);
		this.add(b7);
		this.add(b8);
		this.add(b9);
		this.add(b0);
		this.add(mas);
		this.add(menos);
		this.add(igual);
		this.add(cE);
		this.add(multiplicacion);
		this.add(division);
		this.add(inverso);
		this.add(potencia2);
		this.add(raizCuadrada);
		this.add(raizCubica);
		this.add(seno);
		this.add(coseno);
		this.add(tangente);
		this.add(e);
		this.add(pi);

                salir.addActionListener(this);
 
                b0.addActionListener(this);

                b1.addActionListener(this);

                b2.addActionListener(this);

                b3.addActionListener(this);

                b4.addActionListener(this); // // <== Método que se invoca cuando se hace click sobre la tecla 4
               
                b5.addActionListener(this);

                b6.addActionListener(this);

                b7.addActionListener(this);

                b8.addActionListener(this);

                b9.addActionListener(this);

                mas.addActionListener(this);

                menos.addActionListener(this);
                
                igual.addActionListener(this);
                multiplicacion.addActionListener(this);

                division.addActionListener(this);
                inverso.addActionListener(this);
                potencia2.addActionListener(this);
                raizCuadrada.addActionListener(this);
                raizCubica.addActionListener(this);
                seno.addActionListener(this);
                coseno.addActionListener(this);
				tangente.addActionListener(this);
                e.addActionListener(this);
                pi.addActionListener(this);
                // Al ser una tecla con dos símbolos en la cara le asignamos
                // un Listener diferente
                
                cE.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                procesarCe(); // <== Método que se invoca cuando se hace click sobre la opción tecla Ce
                }});
                
                
		class MyWindowAdapter extends WindowAdapter
		{
			public void windowClosing(WindowEvent e)
			{
				exit();
			}
		}
		addWindowListener(new MyWindowAdapter());

	}
        
        
        // Gestor de eventos
        
	public void actionPerformed(ActionEvent objetoEvento)
	{
		Object fuenteDelEvento = objetoEvento.getSource();

		// Identifica sobre qué objeto generó el evento

		if(fuenteDelEvento == salir) exit();  // Cierra el Programa

		String teclazo = objetoEvento.getActionCommand();

                // Cada botón tiene un simbolo numérico o operador en la cara
                // Se obtiene con charAt
		char simbolo = teclazo.charAt(0);
                
		if( (simbolo >= '0' && simbolo <= '9') || simbolo == '.') // En caso de número
		{
                    if(nuevo) display.setText(""); // Si es una nueva cifra se borra el display
		    display.setText(display.getText()+simbolo);
		    nuevo = false; // Se pone en falso cuando se pone el primer dígito de una cifra
		}
                else if(simbolo=='+'||simbolo=='-'||simbolo=='*'||simbolo=='/' || simbolo == 'x' ||
						simbolo== 'A' || simbolo== 'B' || simbolo=='P' || simbolo== 'e' ||
						simbolo== 'S' || simbolo== 'C' ||simbolo=='T' || simbolo== 'I') // En caso de operador
		{
			double numero = Double.parseDouble(display.getText());

			casio.operacion(numero,simbolo);         // Invoca la funcionalidad de la calculadora

			display.setText(""+casio.getMemoria());  // Obtiene el estado de la memoria de la calculadora

			nuevo = true;
		}
                else if(simbolo=='C') 
                {    
                    casio.clearMemory();
                    display.setText("");
                }
 	}

        // Salir
        public void salir(java.awt.event.ActionEvent evt)
        {
            exit();
        }

        public void exit()
        {
            int respuesta = JOptionPane.showConfirmDialog(rootPane, "Desea salir?","ESCOM",JOptionPane.YES_NO_OPTION);
            if(respuesta==JOptionPane.YES_OPTION) System.exit(0);
        }
        
        public void procesarCe()
        {
            // Codigo para procesar CE
            display.setText("");
            nuevo=true;
        }    
}
