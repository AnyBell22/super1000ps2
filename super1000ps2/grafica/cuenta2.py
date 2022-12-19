from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox




class Cuenta():
    def __init__(self, root):
        self.root=root
        self.root.title("Mi Cuenta")
        #root.geometry("610x400")


        #________________fram3____________para mostrar lo de los botones
        self.frame3=tk.LabelFrame(self.root, text="", width=460, height=500, bg="bisque3")
        self.frame3.pack(ipadx=10, ipady=10, side="right", expand=True, fill="both")

        #___ Frame 1______________________para menu Lateral
        self.frame1=tk.LabelFrame(self.root, text="Perfil Usuario", width=150, height=220, bg="bisque3")
        self.frame1.pack(ipadx=10, ipady=10, expand=True, fill="y")

        #___________________Frame2___________ cerrar sesion
        self.frame2=tk.LabelFrame(self.root, text="", width=150, height=70, bg="bisque3")
        self.frame2.pack(ipadx=10, ipady=10, side="bottom")

        #Creo menu con notebook
        #Creo los Botones
        self.perfil=tk.Button(self.frame1,text="Perfil",command=self.pantalla_perfil)
        self.direccion=tk.Button(self.frame1,text="Direccion",command=self.pantalla_direccion)
        self.pedidos=tk.Button(self.frame1,text="Pedidos",command=self.pantalla_pedidos)
        self.comprobantes=tk.Button(self.frame1,text="Comprobantes",command=self.pantalla_comprobantes)
        self.perfil.place(relx=0.1, rely=0, width=140, height=30)
        self.direccion.place(relx=0.1, rely=0.25, width=140, height=30)
        self.pedidos.place(relx=0.1, rely=0.5, width=140, height=30)
        self.comprobantes.place(relx=0.1, rely=0.75, width=140, height=30)

        #creo el panel notebook
        self.panel=ttk.Notebook(self.frame3, style="TNotebook")
        self.panel.pack(fill="both", expand=True)

        #Estilo de panel y pestañas(para q no se vean)
        estilo_panel=ttk.Style()
        estilo_panel.configure("TNotebook", background="bisque3", foreground="bisque3", padding=0, borderwidth=0)
        estilo_panel.theme_use("default")
        estilo_panel.configure("TNotebook",background="bisque3",foreground="bisque3", borderwidth=0)
        estilo_panel.configure("TNotebook.Tab",background="bisque3",foreground="bisque3", borderwidth=0)
        estilo_panel.map("TNotebook",background=[("selected", "bisque3")])
        estilo_panel.map("TNotebook.Tab",background=[("selected", "bisque3")], foreground=[("selected", "bisque3")])
        
        #Creo las pestañas del panel
        self.p1=tk.Frame(self.panel, background="bisque3")
        self.p2=tk.Frame(self.panel, background="bisque3")
        self.p3=tk.Frame(self.panel, background="bisque3") 
        self.p4=tk.Frame(self.panel, background="bisque3")
        self.p5=tk.Frame(self.panel, background="bisque3")

        #Agrego las pestañas al panel
        self.panel.add(self.p1, text="Administrador")
        self.panel.add(self.p2, text="Perfil")
        self.panel.add(self.p3, text="Direccion")
        self.panel.add(self.p4, text="Pedidos")
        self.panel.add(self.p5, text="Comprobantes")

        self.panel.pack(padx=10, pady=10)
        
        #Agrego los elementos en cada pestaña(funcionalidades)
        #Ventana principal
        self.titulo=tk.Label(self.p1,text="Cuenta Empleado - Usuario - Foto", bg="bisque3")
        self.titulo.pack(expand=1)

        #Ventana perfil
        self.titulo=tk.Label(self.p2,text="Mi Perfil - Otros Datos", bg="bisque3")
        self.titulo.pack(expand=1)
        #Ventana Direccion
        self.dir=tk.Label(self.p3, text="Direccion: xxxxxxxxxxx")
        self.dir.pack(expand=1)
        #Ventana Pedidos
        self.dir=tk.Label(self.p4, text="Pedidos")
        self.dir.pack(expand=1)
        #Ventana Comprobantes
        self.dir=tk.Label(self.p5, text="Comprobantes")
        self.dir.pack(expand=1)

        #creo boton cerrar sesion
        self.cerrar=tk.Button(self.frame2,text="Cerrar Sesion",command=self.cerrarSesion)
        self.cerrar.place(relx=.5,rely=.5,anchor='center',width=140, height=30)


    def cerrarSesion(self):
        messagebox.askyesno(message="¿Seguro que desea cerrar sesion?")
        self.root.destroy()

    def pantalla_perfil(self):
        self.panel.select([self.p2])
        
    def pantalla_direccion(self):
        self.panel.select([self.p3])

    def pantalla_pedidos(self):
        self.panel.select([self.p4])

    def pantalla_comprobantes(self):
        self.panel.select([self.p5])
        
        


if __name__ == "__main__":
    root = tk.Tk()
    app=Cuenta(root)
    root.mainloop()