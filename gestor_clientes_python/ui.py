from tkinter import *
from tkinter import ttk  # Importando los widgets extendidos
from tkinter.messagebox import askokcancel, WARNING
import helpers
import database as db

# Clase para centrar widgets en la pantalla
class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

# Ventana de Creación del cliente 
class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cliente")
        self.build()
        self.center()
        # Nos obligarán a realizar acción en la subventana, bloquea la ventana principal hasta cerrar la subventana
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Configuración del marco principal para la ventana de creación
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Etiquetas para los campos de entrada
        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Nombre (3 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellidos (3 a 30 chars)").grid(row=0, column=2)
        
        # Campos de entrada para DNI, nombre y apellidos
        self.dni_entry = Entry(frame)
        self.dni_entry.grid(row=1, column=0)
        self.dni_entry.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        
        self.nombre_entry = Entry(frame)
        self.nombre_entry.grid(row=1, column=1)
        self.nombre_entry.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        
        self.apellidos_entry = Entry(frame)
        self.apellidos_entry.grid(row=1, column=2)
        self.apellidos_entry.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        # Botones para crear y cancelar
        frame = Frame(self)
        frame.pack(pady=10)

        self.crear_button = Button(frame, text="Crear", command=self.create_client)
        self.crear_button.configure(state=DISABLED)  # Botón deshabilitado inicialmente
        self.crear_button.grid(row=0, column=0)

        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Inicialización de validaciones
        self.validaciones = [0, 0, 0]

    def create_client(self):
        # Obtener datos de los campos de entrada
        dni = self.dni_entry.get()
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        
        if all(self.validaciones):  # Verifica si todos los campos son válidos
            # Crear un nuevo cliente y agregarlo a la base de datos
            nuevo_cliente = db.Cliente(dni, nombre, apellidos)
            db.Clientes.crear(dni, nombre, apellidos)

            # Actualizar la vista en la ventana principal
            self.master.treeview.insert(
                parent='', index='end', iid=dni,
                values=(dni, nombre, apellidos)
            )
            self.close()

    def close(self):
        self.destroy()

    def validate(self, event, index):
        valor = event.widget.get()
        if index == 0: 
            # Validar DNI
            valido = helpers.dni_valido(valor, db.Clientes.lista)
            if valido:
                event.widget.configure(bg="Green")
            else: 
                event.widget.configure(bg="Red")
        elif index == 1: 
            # Validar nombre
            if 3 <= len(valor) <= 30:
                event.widget.configure(bg="Green")
                valido = 1
            else:
                event.widget.configure(bg="Red")
                valido = 0
        elif index == 2: 
            # Validar apellidos
            if 3 <= len(valor) <= 30:
                event.widget.configure(bg="Green")
                valido = 1
            else:
                event.widget.configure(bg="Red")
                valido = 0

        # Actualización de la lista de validaciones
        self.validaciones[index] = valido
        # Habilitar botón si todos los campos son válidos
        self.crear_button.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)

# Ventana de Modificación del cliente 
class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actualizar cliente")
        self.build()
        self.center()
        # Nos obligarán a realizar acción en la subventana, bloquea la ventana principal hasta cerrar la subventana
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Configuración del marco principal para la ventana de edición
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Etiquetas para los campos de entrada
        Label(frame, text="DNI (no editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (3 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellidos (3 a 30 chars)").grid(row=0, column=2)
        
        # Campos de entrada para DNI, nombre y apellidos
        self.dni_entry = Entry(frame)
        self.dni_entry.grid(row=1, column=0)
      
        
        self.nombre_entry = Entry(frame)
        self.nombre_entry.grid(row=1, column=1)
        self.nombre_entry.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        
        self.apellidos_entry = Entry(frame)
        self.apellidos_entry.grid(row=1, column=2)
        self.apellidos_entry.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        # Rellenar los campos con los datos del cliente seleccionado
        cliente = self.master.treeview.focus()
        if cliente:
            campos = self.master.treeview.item(cliente, 'values')
            self.dni_entry.insert(0, campos[0])
            self.nombre_entry.insert(0, campos[1])
            self.apellidos_entry.insert(0, campos[2])

        # Botones para actualizar y cancelar
        frame = Frame(self)
        frame.pack(pady=10)

        self.actualizar_button = Button(frame, text="Actualizar", command=self.edit_client)
        self.actualizar_button.grid(row=0, column=0)

        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Inicialización de validaciones
        self.validaciones = [1, 1]  # Solo nombre y apellidos son válidos

    def edit_client(self):
        # Obtener datos actualizados
        dni = self.dni_entry.get()
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()

        if all(self.validaciones):  # Verifica si todos los campos son válidos
            # Actualizar el cliente en la base de datos
            cliente_modificado = db.Clientes.modificar(dni, nombre, apellidos)

            # Actualizar la vista en la ventana principal
            self.master.treeview.item(self.master.treeview.focus(), values=(dni, nombre, apellidos))
            self.close()

    def close(self):
        self.destroy()

    def validate(self, event, index):
        valor = event.widget.get()
        if index == 0: 
            # Validar nombre
            if 3 <= len(valor) <= 30:
                event.widget.configure(bg="Green")
                valido = 1
            else:
                event.widget.configure(bg="Red")
                valido = 0
        elif index == 1: 
            # Validar apellidos
            if 3 <= len(valor) <= 30:
                event.widget.configure(bg="Green")
                valido = 1
            else:
                event.widget.configure(bg="Red")
                valido = 0

        # Actualización de la lista de validaciones
        self.validaciones[index] = valido
        # Habilitar botón si todos los campos son válidos
        self.actualizar_button.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)

# Clase principal de la aplicación, hereda de Tk y CenterWidgetMixin
class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()  # Centra la ventana al iniciarla

    def build(self):
        # Configuración del marco principal para la ventana principal
        frame = Frame(self)
        frame.pack()

        # Configuración de una tabla para mostrar clientes
        self.treeview = ttk.Treeview(frame, columns=('DNI', 'Nombre', 'Apellidos'))
        self.treeview.pack(side=LEFT, fill=BOTH, expand=True)

        # Configuración de columnas
        self.treeview.column("#0", width=0, stretch=NO)
        self.treeview.column("DNI", anchor=CENTER)
        self.treeview.column("Nombre", anchor=CENTER)
        self.treeview.column("Apellidos", anchor=CENTER)

        # Encabezados de las columnas
        self.treeview.heading("DNI", text="DNI", anchor=CENTER)
        self.treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        self.treeview.heading("Apellidos", text="Apellidos", anchor=CENTER)

        # Configuración de la barra lateral
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Se itera en la base de datos para rellenar la tabla de la UI
        for cliente in db.Clientes.lista:
            self.treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellidos))

        # Botones para crear, modificar y borrar clientes
        frame = Frame(self)
        frame.pack(pady=20)
        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

    def delete(self):
        # Eliminar un cliente de la base de datos y de la vista
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon=WARNING
            )

            if confirmar:
                self.treeview.delete(cliente)
                # Eliminar el cliente de la base de datos aquí
                db.Clientes.borrar(campos[0])

    def create(self):
        # Crear una nueva ventana para añadir un cliente
        CreateClientWindow(self)

    def edit(self):
        # Crear una ventana para editar un cliente si hay uno seleccionado
        if self.treeview.focus():
            EditClientWindow(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
