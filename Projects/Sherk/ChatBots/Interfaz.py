from tkinter import *
from bot import respuesta, nombre
import tkinter as tk
BG_GRAY = "#641E16"
BG_COLOR = "#54CA20"
TEXT_COLOR = "#641E16"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

ventana = Tk()
        
def enter(event):
hi    mensaje = mensajeEntrada.get()
    entrada(mensaje, "Tu")

ventana.title("Sherk")
ventana.resizable(width=False, height=False)
ventana.configure(width=470, height=550, bg=BG_COLOR)
        
# head label
titulo = Label(ventana, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Sherk", width=10, bd=1, font=FONT_BOLD, pady=10)
titulo.place(relwidth=1)
        
# tiny divider
division = Label(ventana, width=450, bg=BG_GRAY)
division.place(relwidth=1, rely=0.07, relheight=0.012)
        
# text widget
tipoLetra = Text(ventana, width=20, height=2, bg=BG_COLOR, 
                                font=FONT, padx=5, pady=5)
tipoLetra.place(relheight=0.745, relwidth=1, rely=0.08)
tipoLetra.configure(cursor="arrow", state=DISABLED)
        
# scroll bar
scroll = Scrollbar(tipoLetra)
scroll.place(relheight=1, relx=0.974)
scroll.configure(command=tipoLetra.yview)
        
# bottom label
boton = Label(ventana, bg=BG_GRAY, height=80)
boton.place(relwidth=1, rely=0.825)
        
# message entry box
mensajeEntrada = Entry(boton, bg="#54CA20", font=FONT)
mensajeEntrada.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
mensajeEntrada.focus()
mensajeEntrada.bind("<Return>", enter)
        
# send button
boton2 = Button(boton, text="Enter", font=FONT_BOLD, width=20, bg=BG_GRAY,
                    command=lambda: enter(None))
boton2.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        
def entrada(mensaje, enviado):
    if not mensaje:
        return
        
    mensajeEntrada.delete(0, END)
    msg1 = f"{enviado}: {mensaje}\n\n"
    tipoLetra.configure(state=NORMAL)
    tipoLetra.insert(END, msg1)
    tipoLetra.configure(state=DISABLED)
        
    msg2 = f"{nombre}: {respuesta(mensaje)}\n\n"
    tipoLetra.configure(state=NORMAL)
    tipoLetra.insert(END, msg2)
    tipoLetra.configure(state=DISABLED)
        
    tipoLetra.see(END)

      
ventana.mainloop()