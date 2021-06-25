/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package guibasico;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;


/**
 *
 * @author Macario
 */
public class Vista extends JFrame
{
    
    // Componentes principales
    
    private JTextField jTextCadena = new JTextField();
    private JTextArea jTextCifrado = new JTextArea();
    private JButton jButtonCifrar = new JButton("Cifrar");
    private JButton jButtonLimpiar  = new JButton("Limpiar");
    
        
    public Vista()
    {
        this.setTitle("Mi programa bien prron");
        this.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        this.setBounds(50,50,640,480);
        initComponents();
        this.setVisible(true);
    }
    public void initComponents()
    {
        // Diseña menú
        JMenuBar barraMenus = new JMenuBar();
	JMenu archivo 	  = new JMenu("Archivo");
        JMenuItem abrir   = new JMenuItem("Abrir");
	JMenuItem salir   = new JMenuItem("Salir");
        this.setJMenuBar(barraMenus);
        barraMenus.add(archivo);
        archivo.add(abrir);
        archivo.add(salir);
        
        // Componentes auxiliares
        JLabel etiqueta1 = new JLabel("Cadena:");
        JLabel etiqueta2 = new JLabel("Cifrado:");
        
        // Posiciones de los componentes
        this.setLayout(null); // El programador indica coordenadas y tamaño
        etiqueta1.setBounds(50,100,100,30);
        etiqueta2.setBounds(50,200,300,30);
        jTextCadena.setBounds(100,100,400,30);
        jTextCifrado.setBounds(100,200,400,90);
        jButtonCifrar.setBounds(200,145,100,40);
        jButtonLimpiar.setBounds(320,145,100,40);

         // Características de componentes
        jTextCifrado.setLineWrap(true);  // Para que sea multilinea
        jTextCifrado.setBorder(BorderFactory.createLineBorder(Color.black));
        jTextCifrado.setEditable(false);
        
        // Coloca componentes
        this.add(etiqueta1);
        this.add(etiqueta2);
        this.add(jTextCadena);
        this.add(jTextCifrado);
        this.add(jButtonCifrar);
        this.add(jButtonLimpiar);
        
        // Gestión de eventos
        salir.addActionListener(new java.awt.event.ActionListener() {
        public void actionPerformed(java.awt.event.ActionEvent evt) {
        salir(evt);}});
    
        jButtonCifrar.addActionListener(new java.awt.event.ActionListener() {
        public void actionPerformed(java.awt.event.ActionEvent evt) {
        procesarCifrar(evt);}});
        
        jButtonLimpiar.addActionListener(new java.awt.event.ActionListener() {
        public void actionPerformed(java.awt.event.ActionEvent evt) {
        procesarLimpiar(evt);}});
        
        class MyWindowAdapter extends WindowAdapter
	{
            public void windowClosing(WindowEvent e)
            {
		exit();
            }
	}
        addWindowListener(new MyWindowAdapter());
        
    }        
    
    public void salir(java.awt.event.ActionEvent evt)
    {
        exit();
    }

    public void exit()
    {
        int respuesta = JOptionPane.showConfirmDialog(rootPane, "Desea salir?","Aviso",JOptionPane.YES_NO_OPTION);
        if(respuesta==JOptionPane.YES_OPTION) System.exit(0);
    }
    
    public void procesarCifrar(java.awt.event.ActionEvent evt)
    {
        String textoCapturado = jTextCadena.getText();
        if(textoCapturado.length() > 0 || textoCapturado.length() > 64)
        {    
            String cadenaParaCifrar = jTextCadena.getText();  // Obtenemos la cadena capturara
            String textoCifrado = "Cadena Cifrada aaaaaaaaaaa bbbbbbbbbbbbb ccccccccccccc ddddddddddddddddd eeeeeeeeeeeeeee ffffffffffffff";  // Aquí debes llamar a la funcionalidad para cifrar pasando la cadenaParaCifrar como parámetro
            jTextCifrado.setText(textoCifrado);
        }
        else
           JOptionPane.showConfirmDialog(rootPane, "Error!!", "Aviso" ,JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
    }
    
    public void procesarLimpiar(java.awt.event.ActionEvent evt)
    {
        jTextCadena.setText("");
        jTextCifrado.setText("");
    }
    
    
}
