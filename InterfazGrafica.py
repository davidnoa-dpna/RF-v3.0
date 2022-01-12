from tkinter import *
import time
import os
import cv2
from PIL import Image, ImageTk
import prueba2_0 as pb
import prueba3_0 as pb3
import pruebaModelo as pM
import tkinter.messagebox

class Ventana:


    def __init__(self,ini):


        self.ven = ini
        #self.ven.resizable(False, False) #ventana estable
        self.ven.title('Reconocimiento Facial')  # esta linea se agrego luego
        self.ven.iconbitmap(r'D:\PROYECTOS_PYTHON\Proyecto_ESPOCH\icon\favicon.ico')
        self.path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.var = None
        self.captura = None
        self.variable = None

        self.botones()
        self.ven.mainloop()


    def botones(self):
        if self.captura != None:

            self.captura.release()
            self.prueba.destroy()


        self.ven.geometry('500x350')
        self.cero = Frame(self.ven)
        self.cero.place( relwidth = 1, relheight = 1)
        #self.cero.place(relwidth=1, relheight=1)
        self.cero.config(bg="sky blue")
        btn1_mostrar = Button(self.cero, text="Agregar Usuario",bg="yellow", font = 'Fixedsys',command = lambda:self.asignarNombre()).grid(
        row=2,
        column=1,
        padx=10,
        pady=10)

        btn2_eliminar = Button(self.cero, text="Reconocer", bg= "yellow", font = 'Fixedsys',command = lambda:self.reconocerNombre()).grid(
        row=3,
        column=1,
        padx=10,
        pady=10)

        #btn3_mostarr = Button(self.cero, text="darr",command = lambda:self.botonPrueba()).grid(
        #row=2,
        #column=2)

        txt = Label(self.cero,text= 'SISTEMA DE RECOCIMIENTO FACIAL Y DETECCION DE MASCARILLAS',bg="sky blue", font = 'Fixedsys').grid(
        row=0,
        column=1,
        padx=10,
        pady=10)
        self.listaOpciones()

        self.imagen= PhotoImage(file="D:\PROYECTOS_PYTHON\Proyecto_ESPOCH\img\imagen1.png")
        Label(self.ven,image=self.imagen).place(x=90,y=130)


    #funcion agregar Usuario
    def agregar(self,nombre):
        self.variable = None
        Video = pb.DataBase(nombre,'_sin Tapabocas')
        self.objeto = Video
        self.botonPrueba()
    # elemetos de la interfaz
    def listaOpciones(self):


        self.barraMenu = Menu(self.ven)



        self.ven.config(menu = self.barraMenu,height = 300)


        #a.config(bg = "purple")


        menuAyuda = Menu(self.barraMenu,font = 'Arial 12 bold',tearoff=0)

        menuAyuda.add_command(label="Salir",command=lambda:self.ven.destroy())
        #menuAyuda.add_command(label="Acerca de", command= lambda:self.ven.barraMenu.tkinter.messagebox.showinfo("Acerca de","Esta interfaz fue"))

        menuProject = Menu(self.barraMenu,tearoff=0)
        menuProject.add_command(label="Inicio",command=lambda:self.botones())
        self.barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
        self.barraMenu.add_cascade(label="Proyecto",menu=menuProject)


    def scrolbar(self):

        direccion = f'{self.path_desktop}/Fotos2'
        lista = os.listdir(direccion)
        scrollbar = Scrollbar(self.tercer)
        scrollbar.grid(row=3,
        column=2,
        sticky='NS')
        self.listbox = Listbox(self.tercer, yscrollcommand=scrollbar.set,font = 'Fixedsys')
        for i in lista:
            if i != 'DatosModelos':
                self.listbox.insert("end", str(i))
        self.listbox.grid(row=3,
        column=1)

        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.seleccionar)

    def seleccionar(self,eve):
        if len(self.listbox.curselection())!=0:

            self.list = self.listbox.get(self.listbox.curselection()[0])
            s = str(self.listbox.get(self.listbox.curselection()[0]))
            if  (self.nombre1.get()) != "" :
                self.nombre1.delete("0","end")
            self.nombre1.insert(0,s)


    def barraProgreso(self,frame,maximum,x,y):
        from tkinter import ttk
        s = ttk.Style()
        s.theme_use('classic')

        s.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='#5A504E',
                background='#BF00FF',
            darkcolor="#390439",
            lightcolor="#ED28F0",
            bordercolor="black",
            )
        self.mpb = ttk.Progressbar(frame,orient ="horizontal",
        style="custom.Horizontal.TProgressbar",
        length = 200, mode ="determinate")
        self.textobar = Label(frame,text = "",bg = 'dim gray',font = 'Fixedsys' )
        self.textobar.grid(column = x, row = y )

        self.mpb.grid(column = x, row =y+1 )

        self.mpb["maximum"] = maximum
        self.mpb["value"]  = 0




    #funciones para guardar nombres
    def asignarNombre(self):
        self.barraMenu.destroy()
        self.primer = Frame(self.ven)
        self.primer.place(relwidth=1, relheight=1)
        self.primer.config(bg="sky blue")
        #self.variable = None
        self.nombre = Entry(self.primer,font = 'Fixedsys')
        self.nombre.grid(
        row=1,
        column=3,
        padx=50,
        pady=50)
        #result = self.nombre.get()
        btn1_mostrar = Button(self.primer, text=" Agregar Nombre", bg="yellow", font = 'Fixedsys',
        command = lambda:self.agregar(self.nombre.get()) if (self.nombre.get()) != "" and
        (self.usuarioExistente(self.nombre.get()) == False) else tkinter.messagebox.showinfo("Mensaje:", "¡Por favor, escriba su nombre!"))


        btn1_mostrar.grid(
        row=1,
        column=1,
        padx=5,
        pady=5)

    def usuarioExistente(self,nombre):
        direccion  = f'{self.path_desktop}/Fotos2'
        if not os.path.exists(direccion):
            return False
        print(nombre)
        tkinter.messagebox.showinfo("Mensaje:", "¡Usuario agregado, se procederá a tomar las fotos!")  # agregado hoy

        etiquetas = os.listdir(direccion)

        if nombre in etiquetas:
            tkinter.messagebox.showinfo("Mensaje:","¡Este usuario ya existe!") #agregado hoy
            print('ya existe')
            return True

        return False




    def UsuarioMascarilla(self,nombre):
        #self.primer.destroy()
        self.segundo = Frame(self.ven,width=400, height=200).place(relwidth=1, relheight=1)

        btn_tomarMas = Button(self.segundo, text=" tomar fotos",bg="yellow",font = 'Fixedsys',
        command = lambda:self.video2(nombre ))

        btn_tomarMas.grid(
        row=1,
        column=1,
        padx=5,
        pady=5)

        txt = Label(self.segundo,text= 'coloquese la mascarilla y cuando este listo presione el boton "tomar fotos"',
        font = 'Fixedsys').grid(
        row=2,
        column=1,
        padx=50,
        pady=50)

        txt2 = Label(self.segundo,text= 'esperan aque se cierre y salga modelo creado',
        font = 'Fixedsys').grid(
        row=2,
        column=2,
        padx=50,
        pady=50)

        #self.var = True

        #return self.var #cambioo self.var a true

    def video2(self,nombre): #self.var = false
        self.var = False
        Video2 = pb.DataBase(nombre,'_con Tapabocas')
        self.objeto = Video2
        self.botonPrueba()



    #reconocer
    def reconocerNombre(self):

        self.cero.destroy()
        self.ven.geometry('380x300')
        self.tercer = Frame(self.ven)
        self.tercer.place(relwidth=1, relheight=1)
        self.tercer.config(bg="sky blue")
        #self.list = ''
        self.scrolbar()
        #self.listbox.bind('<<ListboxSelect>>', self.seleccionar)
        #textExample.insert(0, "Default Text")
        self.nombre1 = Entry(self.tercer,font = 'Fixedsys')
        #self.nombre1.insert( self.list)
        self.nombre1.grid(
        row=1,
        column=3,
        padx=25,
        pady=25)
        #result = self.nombre.get()

        btn1_mostrar = Button(self.tercer, text=" Nombre",bg="yellow",font = 'Fixedsys',
        command = lambda:self.reconocerxfat32(self.nombre1.get()) if (self.nombre1.get()) != "" and
        (self.usuarioExistente(self.nombre1.get()) == True) else print('no'))
        btn1_mostrar.grid(
        row=1,
        column=1,
        padx=5,
        pady=5)

        text2 = Label(  self.tercer,text = 'Lista de Usuarios',bg="sky blue",font = 'Fixedsys').grid(
        row=2,
        column=1,
        padx=5,
        pady=5)
    def reconocerxfat32(self ,nombre):#self.variable  = True
        self.barraMenu.destroy()
        self.variable = True
        recon = pb3.Reconocer(nombre)
        self.objeto = recon
        self.botonPrueba()
        self.ven.geometry('720x500')
    # (muestra el Frame de la camera) = funcion(show_vid)
    def botonPrueba(self):
        self.ven.geometry('720x540')
        self.prueba = Frame(self.ven,bg = 'dim gray')
        self.prueba.place(relwidth=1, relheight=1)
        self.lmain = Label(master=self.prueba)
        self.lmain.grid(column=0, rowspan=4, padx=5, pady=5)
        #self.lmain.pack()
        self.barraProgreso(self.prueba,250,0,8)
        self.show_vid()
        #self.barraProgreso()
        if self.variable:
            btn = Button(self.prueba,text = 'salir',bg= "yellow",font = 'Fixedsys', command = lambda:self.botones())
            btn.grid(
            row=1,
            column=2,
            padx=10,
            pady=10)



        #self.UsuarioMascarilla('sdsdsdsd')
    # guardar Modelos
    def guardarModelos(self): # self.var = None

        print('estoy aquiiiiiiiiiiiiiiiiii')
        #tkinter.messagebox.showinfo("Mensaje:", "Modelo creado y entrenado")  # agregado hoy
        self.btn_4["state"] = "disabled"
        self.prueba.destroy()
        self.ven.geometry('320x300')
        modelo = pM.modelo(self.nombre.get())
        self.barraProgreso(self.prueba2,7,0,1)
        rostro, array,nombre = modelo.reco()
        reconocimiento = cv2.face.LBPHFaceRecognizer_create()
        for i in range(1,8):
            c = "{0:.0f}".format(((i/7)*100))
            self.textobar['text'] = 'Guardando datos '+c
            self.mpb["value"] = i
            self.prueba2.update()
            if i == 5 :
                #----Entrenamos el modelo----
                reconocimiento.train(rostro, array)
                #----Guardamos el modelo----
                reconocimiento.write(f'{self.path_desktop}/Fotos2/DatosModelos/Modelo{nombre}.xml')
                print("Modelo creado")
                tkinter.messagebox.showinfo("Mensaje:", "Modelo creado")  # agregado hoy
            else:
                time.sleep(0.5)
        self.botones()
        self.var = None
    # Activar frame dentro de la ventana
    def show_vid(self):
        #cap = cv2.VideoCapture(0)
        #frame = op.oooo()
        #self.lista.append(con)
        if self.variable != True:
            frame,con,cap = self.objeto.VideoCaptura()
            if con != 250:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.lmain.imgtk = imgtk
                self.lmain.configure(image=imgtk)
                self.lmain.after(20, self.show_vid)
                self.prueba.update_idletasks()
                self.mpb["value"]  = con
                self.textobar['text']= 'Tomando Fotos...'
                self.captura = cap

            else:
                cap.release()
                self.prueba.destroy()
                if self.var == None:
                    self.ven.geometry('300x300')
                    self.UsuarioMascarilla(self.nombre.get())

                if self.var == False  and cap.isOpened() == False:
                    self.prueba2 = Frame(self.ven)
                    self.prueba2.place(relwidth=1, relheight=1)
                    self.ven.geometry('300x300')
                    self.btn_4 = Button(self.prueba2, text="Guardar",bg= "yellow",font = 'Fixedsys'
                    ,command = lambda:self.guardarModelos())
                    self.btn_4.grid(
                    column = 0,
                    row = 0,
                    padx = 25,
                    pady = 25)

                    #print(len(self.lista))
        else:
            self.mpb.destroy()
            self.textobar.destroy()
            frame,cap  = self.objeto.inicioReconocer()
            if cap != False :
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.lmain.imgtk = imgtk
                self.lmain.configure(image=imgtk)
                self.lmain.after(20, self.show_vid)
                self.captura = cap

            else:
                tkinter.messagebox.showinfo("Mensaje", "¡Ha ocurrido un error!")  # agregado hoy
                print('a ocurrido un  errorwwwwwwwwwwwwwwwww')
                self.captura.release()
                self.prueba.destroy()
            #print(self.captura, cap.isOpened())
            #if cap.isOpened() == False :
                #print('a ocurrido un  errorwwwwwwwwwwwwwwwww')
                #self.captura.release()
                #self.prueba.destroy()








































Ventana = Ventana(Tk())
