from tkinter import *

pi = 3.1416
me = Tk()
me.title("Ventana para calculo de circulos")
pantalla = Entry(me)
pantalla.grid(row=1, columnspan=22, sticky=W+E)

def entra_pantalla (n):
    pantalla.insert(1, n)
    
def limpia_pantalla():
    pantalla.delete(0, END)
    
def lee_radio():
    global diametro
    global radio
    global area
    global perimetro
    lee_pantalla_radio = int (pantalla.get())
    radio = lee_pantalla_radio
    diametro = radio+radio
    area = pi * (radio**2)
    perimetro = 2 * pi * radio
    limpia_pantalla()
    
Button(me, text = "DIAMETRO", command = lambda:entra_pantalla(" Diametro ="+str(diametro))).grid(row=2, column=0, sticky=W+E)
Button(me, text = "PERIMETRO", command = lambda:entra_pantalla(" Perimetro ="+str(diametro))).grid(row=2, column=20, sticky=W+E)
Button(me, text = "AREA", command = lambda:entra_pantalla(" Area ="+str(diametro))).grid(row=3, column=0, sticky=W+E)
Button(me, text = "BORRAR", command = lambda:limpia_pantalla()).grid(row=3, column=20, sticky=W+E)
Button(me, text = "LEER RADIO", command = lambda:lee_radio()).grid(row=4, column=0, sticky=W+E)

me.mainloop()
