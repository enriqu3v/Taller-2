from os import remove
from playsound import playsound
from gtts import gTTS
import random
import string
from textwrap import fill
from tkinter import *

speech = gTTS(text="Bienvenido al programa de alfabetos y Lenguajes:",lang="es")
speech.save("archivo.mp3")
playsound("archivo.mp3")
remove("archivo.mp3")

#############################     ALFABETO     ##################################################

class Alfabeto():

  def __init__(self, cadenaString1, cadenaString2): 
    self.listAlfa1 = cadenaString1.split()
    self.listAlfa2 = cadenaString2.split()

  def get_listAlfa1(self):
    return self.listaAlfa1

  def get_listAlfa2(self):
    return self.listaAlfa2


  def union(self, a1, a2):
    a = set (a1)
    b = set (a2)

    union=list(a|b)

    #print (union)
    resultado.set(union)
    mensaje= " ".join(union)
    speech = gTTS(text="se escogio la opcion de realizar la union de los alfabetos 1 y 2 y el resultado de la unión es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")

  def restaAb(self, a1, a2):

    a = set (a1)
    b = set (a2)

    diferenciaAB=list(a-b)
    #print (diferenciaAB)
    resultado.set(diferenciaAB)
    mensaje= " ".join(diferenciaAB)
    speech = gTTS(text="se escogio la opcion de realizar la resta entre 1 y 2 y el resultado de la diferencia de 1 menos 2 es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")

  def restaBa(self, a1, a2):

    a = set (a1)
    b = set (a2)

    diferenciaBA=list(b-a)
    #print (diferenciaAB)
    resultado.set(diferenciaBA)
    mensaje= " ".join(diferenciaBA)
    speech = gTTS(text="se escogio la opcion de realizar la resta entre 2 y 1 y el resultado de la diferencia de 2 menos 1  es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")


  def intercepcion(self, a1, a2):

    a = set (a1)
    b = set (a2)

    intercepcion=list(a & b)
    #print(intercepcionAB)
    resultado.set(intercepcion)
    mensaje= " ".join(intercepcion)
    speech = gTTS(text="se escogio la opcion de realizar la intercepción de 1 y 2 y el resultado de la intercepción es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")


  def cerraduraAsterisco(self, a1, potencia):

    acumPalabra = ""
    listAlfaEstre = []

    listAlfaEstre.append("VACIO") 
    for i in range(potencia):

      for j in range(len(a1)):

        for k in range(i+1):
          acumPalabra = acumPalabra + a1[j]
        
        listAlfaEstre.append(acumPalabra) 
        acumPalabra=""

    #print(estrellaAlfabeto)
    resultado.set(listAlfaEstre)
    mensaje= " ".join(listAlfaEstre)
    speech = gTTS(text="se escogio la opcion de realizar la cerradura de estrella y el resultado de la cerradura de estrella del alfabeto 1 es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")
    listAlfaEstre.clear()
    


  def __str__(self):
    return "%s, %s" %(self.listAlfa1, self.listAlfa2)  



#############################     LENGUAJE     ##################################################


class Lenguaje(Alfabeto):

  def __init__(self, listAlfabeto1, listAlfabeto2): 
    self.listAlfabeto1 = listAlfabeto1
    self.listAlfabeto2 = listAlfabeto2
    self.listLeng1 = []
    self.listLeng2 = []


  def crearLenguaje1(self, listAlfabeto, cantPal):
    listLeng = []
    acumPalabra = ""

    for i in range(cantPal): 

      cantCarac = random.randint(1, 6) 

      for j in range(cantCarac):
        random.shuffle(listAlfabeto) 
        acumPalabra = acumPalabra + listAlfabeto[0] 
            
      listLeng.append(acumPalabra)
      acumPalabra = "" 
      #print(lenguaje)

    mostrarL1.set(listLeng)
    mensaje= " ".join(listLeng)
    speech = gTTS(text="se escogio la opcion de realizar la creacion del lenguaje a partir del alfabeto 1 y el lenguaje 1 es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")
    listLeng.clear() 

  def crearLenguaje2(self, listAlfabeto, cantPal):
    listLeng = []
    acumPalabra = ""

    for i in range(cantPal): 

      cantCarac = random.randint(1, 6) 

      for j in range(cantCarac):
        random.shuffle(listAlfabeto) 
        acumPalabra = acumPalabra + listAlfabeto[0] 
            
      listLeng.append(acumPalabra)
      acumPalabra = "" 
      #print(lenguaje)

    mostrarL2.set(listLeng)
    mensaje= " ".join(listLeng)
    speech = gTTS(text="se escogio la opcion de realizar la creacion del lenguaje a partir del alfabeto 2 y el lenguaje 2 es :"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")
    listLeng.clear() 


  def potencia(self, l1, indPotencia): 

    acumPalabra = ""
    listLengPoten = []

    for j in range(len(l1)): 

      for k in range(indPotencia):
        acumPalabra = acumPalabra + l1[j]
        
      listLengPoten.append(acumPalabra) 
      acumPalabra=""

    resultado.set(listLengPoten)
    mensaje= " ".join(listLengPoten)
    speech = gTTS(text="se escogio la opcion de realizar la potencia del lenguaje y la potencia es :"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")
    listLengPoten.clear()  



  def __str__(self):
    return "%s, %s" %(self.listLeng1, self.listLeng2)  



#############################     OPERACIONES ALFABETO     ##################################################


class operacionesAlfabeto(Alfabeto): 

  def union():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.union(obj1.listAlfa1, obj1.listAlfa2)


  def restaAB():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.restaAb(obj1.listAlfa1, obj1.listAlfa2)
      

  def restaBA():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.restaBa(obj1.listAlfa1, obj1.listAlfa2) 


  def intercepcion():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.intercepcion(obj1.listAlfa1, obj1.listAlfa2)


  def cerraduraAsteriscoAlfa1():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.cerraduraAsterisco(obj1.listAlfa1, int(potenciaCerradura.get())) 


  def cerraduraAsteriscoAlfa2():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())

    obj1.cerraduraAsterisco(obj1.listAlfa2, int(potenciaCerradura.get())) 



#############################     OPERACIONES LENGUAJE     ##################################################

class operacionesLenguaje(Lenguaje, Alfabeto): 

  def crearLeng1():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2)


    obj2.crearLenguaje1(obj1.listAlfa1, int(PalabL1.get())) 


  def crearLeng2():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2)


    obj2.crearLenguaje2(obj1.listAlfa2, int(PalabL2.get())) 


  def union():
    lengu1 = mostrarL1.get()
    lengu2 = mostrarL2.get()
    unionlengu=lengu1 + lengu2 
    resultado.set(unionlengu)
    mensaje= " ".join(unionlengu)
    speech = gTTS(text="se escogio la opcion de realizar la union de los lenguajes 1 y 2 y el resultado de la unión es:"+mensaje,lang="es")
    speech.save("archivo.mp3")
    playsound("archivo.mp3")
    remove("archivo.mp3")

  def restaAB():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2) 

    obj2.restaAb(mostrarL1.get().split(), mostrarL2.get().split())


  def restaBA():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2) 

    obj2.restaBa(mostrarL1.get().split(), mostrarL2.get().split())


  def intercepcion():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2) 

    obj2.intercepcion(mostrarL1.get().split(), mostrarL2.get().split())


  def potenciaLenguaje():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2) 

    obj2.potencia(mostrarL1.get().split(), int(potenciaLeng.get()))

  def potenciaLenguaje2():

    obj1 = Alfabeto(Alfabeto1.get(), Alfabeto2.get())
    obj2 = Lenguaje(obj1.listAlfa1, obj1.listAlfa2) 

    obj2.potencia(mostrarL2.get().split(), int(potenciaLeng2.get()))  

  def invertirA():
    listareves = mostrarL1.get()
    invertir= list(listareves)
    invertir.reverse()
    resultado.set(invertir)

  def invertirB():
    listareves = mostrarL2.get()
    invertir= list(listareves)
    invertir.reverse()
    resultado.set(invertir)

  def cardinalidadA():
    listaCopia = []
    cont=0
    listaLenguaje = mostrarL1.get().split()

    for j in listaLenguaje: 
      for k in j:
        if(k!="(" and k!=")" and k!="," and k!="'"):
          cont=cont+1

      listaCopia.append(cont)
      cont=0   


    resultado.set(listaCopia)
  def cardinalidadB():
    listaCopia = []
    cont=0
    listaLenguaje = mostrarL2.get().split()

    for j in listaLenguaje: 
      for k in j:
        if(k!="(" and k!=")" and k!="," and k!="'"):
          cont=cont+1

      listaCopia.append(cont)
      cont=0   


    resultado.set(listaCopia)

class CambioDeLenguaje(): 

  def ingles():

    textAlfab1.set("A - alphabet #1")
    textAlfab2.set("B - alphabet #2")
    textUnionAlfa.set("UNION - A U B")
    textIntercepAlfa.set("intercept - A ∩ B")
    textDifeAbAlfa.set("difference (A - B)")
    textDifeBaAlfa.set("difference (B - A)")
    textCerraduraAlfa.set("ENTER THE POWER FOR THE STAR LOCK")
    textCerraduraAlfaA.set("STAR LOCK - A")
    textCerraduraAlfaB.set("STAR LOCK - B")
    textCantidadPalL1.set("amount. words - L1")
    textCantidadPalL2.set("amount. words - L2")
    textCrearLeng1.set("create language #1")
    textCrearLeng2.set("create language #2")

    textUnionLeng.set("UNION - L1 U L2")
    textDifeLengL1L2.set("difference (L1 - L2)")
    textDifeLengL2L1.set("difference (L2 - L1)")

    textInterLeng.set("invest - L1 L2")
    textInvertLengL1.set("invest - L1")
    textInvertLengL2.set("invest - L2")

    textCardinalLengL1.set("cardinality - L1")
    textCardinalLengL2.set("cardinality - L2")


    textPotenLengL1.set("type the power of L1")
    textPotenLengL2.set("type the power of L2")

    textCalPotenLengL1.set("calculate the power of L1")
    textCalPotenLengL2.set("calculate the power of L2")
    textResultado.set("OUTPUT")


  def espanol():
    return 0

venta = Tk()
venta.geometry("900x900")
venta.title("Taller #2 - Compiladores")
venta.configure(background="black")
venta.resizable(False,False)
main_title = Label(text="OPERACIONES ENTRE ALFABETOS Y LENGUAJES",bg="black",fg="#0DBFF8")
main_title.pack()

Alfabeto1 = StringVar()
Alfabeto2 = StringVar()

PalabL1 = StringVar()
PalabL2 = StringVar()
mostrarL1 = StringVar()
mostrarL2 = StringVar()
potenciaLeng = StringVar()
potenciaLeng2 = StringVar()
resultado = StringVar()
potenciaCerradura = StringVar()

textIngles = "English"
textEspanol = "Spanish"
textAlfab1 = "A = ALFABETO #1"
textAlfab2 = "B = ALFABETO #2"
textUnionAlfa = "UNION - A U B"
textIntercepAlfa = "INTERCEPCION - A ∩ B"
textDifeAbAlfa = "DIFERENCIA (A - B)"
textDifeBaAlfa = "DIFERENCIA (B - A)"
textCerraduraAlfa = "DIGITE LA POTENCIA PARA LA CERRADURA ESTRELLA"
textCerraduraAlfaA = "CERRADURA ESTRELLA - A"
textCerraduraAlfaB = "CERRADURA ESTRELLA - B"
textCantidadPalL1 = "CANT. PALABRAS - L1"
textCantidadPalL2 = "CANT. PALABRAS - L2"
textCrearLeng1 = "CREAR LENGUAJE #1"
textCrearLeng2 = "CREAR LENGUAJE #2"

textUnionLeng = "UNION - L1 U L2"
textDifeLengL1L2 = "DIFERENCIA (L1 - L2)"
textDifeLengL2L1 = "DIFERENCIA (L2 - L1)"

textInterLeng = "INTERSECCION - L1 L2"
textInvertLengL1 = "INVERTIR - L1"
textInvertLengL2 = "INVERTIR - L2"

textCardinalLengL1 = "CARDINALIDAD - L1"
textCardinalLengL2 = "CARDINALIDAD - L2"


textPotenLengL1 = "DIGITE LA POTENCIA DE L1"
textPotenLengL2 = "DIGITE LA POTENCIA DE L2"

textCalPotenLengL1 = "CALCULAR POTENCIA L1"
textCalPotenLengL2 = "CALCULAR POTENCIA L2"
textResultado = "RESULTADO"

boton_btn = Button(venta,text=textIngles,command=CambioDeLenguaje.ingles,width="30",height="1",bg="black",fg="#0DBFF8").place(x=340,y= 30)
boton_btn = Button(venta,text=textEspanol,command=CambioDeLenguaje.espanol,width="30",height="1",bg="black",fg="#0DBFF8").place(x=340,y= 50)

Alfabeto1_label = Label(text=textAlfab1,bg="black",fg="#0DBFF8").place(x=340,y=70)

Alfabeto2_label = Label(text=textAlfab2,bg="black",fg="#0DBFF8").place(x=340,y=130)


Alfabeto1_entry = Entry(textvariable=Alfabeto1, width="40",bg="black",fg="#0DBFF8").place(x=260, y = 100)

Alfabeto2_entry = Entry(textvariable=Alfabeto2, width="40",bg="black",fg="#0DBFF8").place(x=260, y = 160)



boton_btn = Button(venta,text=textUnionAlfa,command=operacionesAlfabeto.union,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 200)

boton_btn = Button(venta,text=textIntercepAlfa,command=operacionesAlfabeto.intercepcion,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 250)

boton_btn = Button(venta,text=textDifeAbAlfa,command=operacionesAlfabeto.restaAB,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 300)

boton_btn = Button(venta,text=textDifeBaAlfa,command=operacionesAlfabeto.restaBA,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 350)


Alfabeto1_label = Label(text=textCerraduraAlfa,bg="black",fg="#0DBFF8").place(x=22,y=400)

Alfabeto1_entry = Entry(textvariable=potenciaCerradura, width="40",bg="black",fg="#0DBFF8").place(x=22, y = 430)

boton_btn = Button(venta,text=textCerraduraAlfaA,command=operacionesAlfabeto.cerraduraAsteriscoAlfa1,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 470)

boton_btn = Button(venta,text=textCerraduraAlfaB,command=operacionesAlfabeto.cerraduraAsteriscoAlfa2,width="30",height="1",bg="black",fg="#0DBFF8").place(x=22,y= 510)



labelCantPalL1 = Label(text=textCantidadPalL1,bg="black",fg="#0DBFF8").place(x=360,y=210)
cantPalL1 = Entry(textvariable=PalabL1, width="3",bg="black",fg="#0DBFF8").place(x=500, y=210)

boton_btn = Button(venta,text=textCrearLeng1,command=operacionesLenguaje.crearLeng1,width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=240)

lenguajeUno = Entry(textvariable=mostrarL1, width="40",bg="black",fg="#0DBFF8").place(x=500, y=242)



labelCantPalL1 = Label(text=textCantidadPalL2,bg="black",fg="#0DBFF8").place(x=360,y=303)
cantPalL1 = Entry(textvariable=PalabL2, width="3",bg="black",fg="#0DBFF8").place(x=500, y=304)

boton_btn = Button(venta,text=textCrearLeng2,command=operacionesLenguaje.crearLeng2,width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=330)

lenguajeDos = Entry(textvariable=mostrarL2, width="40",bg="black",fg="#0DBFF8").place(x=500, y = 334)

boton_btn = Button(venta,text=textUnionLeng, command=operacionesLenguaje.union, width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=367)
boton_btn = Button(venta,text=textDifeLengL1L2, command=operacionesLenguaje.restaAB, width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=400)
boton_btn = Button(venta,text=textDifeLengL2L1, command=operacionesLenguaje.restaBA, width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=442)
boton_btn = Button(venta,text=textInterLeng, command=operacionesLenguaje.intercepcion, width="20",height="1",bg="black",fg="#0DBFF8").place(x=340, y=484)
boton_btn = Button(venta,text=textInvertLengL1, command=operacionesLenguaje.invertirA, width="20",height="1",bg="black",fg="#0DBFF8").place(x=500, y=484)
boton_btn = Button(venta,text=textInvertLengL2, command=operacionesLenguaje.invertirB, width="20",height="1",bg="black",fg="#0DBFF8").place(x=660, y=484)
boton_btn = Button(venta,text=textCardinalLengL1, command=operacionesLenguaje.cardinalidadA, width="20",height="1",bg="black",fg="#0DBFF8").place(x=500, y=442)
boton_btn = Button(venta,text=textCardinalLengL2, command=operacionesLenguaje.cardinalidadB, width="20",height="1",bg="black",fg="#0DBFF8").place(x=660, y=442)

labelCantPalL1 = Label(text=textPotenLengL1,bg="black",fg="#0DBFF8").place(x=340,y=524)
cantPalL1 = Entry(textvariable=potenciaLeng, width="3",bg="black",fg="#0DBFF8").place(x=500, y=524)

boton_btn = Button(venta,text=textCalPotenLengL1, command=operacionesLenguaje.potenciaLenguaje, width="20",height="1",bg="black",fg="#0DBFF8").place(x=530, y=520)

labelCantPalL1 = Label(text=textPotenLengL2,bg="black",fg="#0DBFF8").place(x=340,y=564)
cantPalL1 = Entry(textvariable=potenciaLeng2, width="3",bg="black",fg="#0DBFF8").place(x=500, y=564)

boton_btn = Button(venta,text=textCalPotenLengL2, command=operacionesLenguaje.potenciaLenguaje2, width="20",height="1",bg="black",fg="#0DBFF8").place(x=530, y=560)

Alfabeto1_label = Label(text=textResultado,bg="black",fg="#0DBFF8") 
Alfabeto1_label.place(x=340,y=600)

mostrar = Entry(textvariable=resultado, width="120",bg="black",fg="#0DBFF8")
mostrar.place(x=35, y = 630)

venta.mainloop()