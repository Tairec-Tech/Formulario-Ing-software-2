import customtkinter as ctk
from tkinter import messagebox

# CONFIGURACIÓN VISUAL (Tema Claro)
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class SistemaBrigadasApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana
        self.title("SGB - Gestión de Brigadas Maracaibo")
        self.geometry("1100x650")

        # Layout Principal: 2 Columnas
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 2. Crear Menú Lateral
        self.crear_menu_lateral()

        # 3. Frame Principal (Área de trabajo)
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Al iniciar, mostramos el Dashboard directamente
        self.mostrar_dashboard()

    def crear_menu_lateral(self):
        self.sidebar = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(8, weight=1)

        # Logo / Título
        lbl_logo = ctk.CTkLabel(self.sidebar, text="BRIGADAS\nMARACAIBO", font=ctk.CTkFont(size=20, weight="bold"))
        lbl_logo.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Botones de Navegación (Módulos Principales)
        # Nota: Se eliminó el botón "Inicio" como pediste.

        self.btn_inst = ctk.CTkButton(self.sidebar, text="Instituciones (2.0)", command=self.menu_instituciones)
        self.btn_inst.grid(row=2, column=0, padx=20, pady=10)

        self.btn_usu = ctk.CTkButton(self.sidebar, text="Usuarios (3.0)", command=self.mostrar_usuarios)
        self.btn_usu.grid(row=3, column=0, padx=20, pady=10)

        self.btn_brig = ctk.CTkButton(self.sidebar, text="Brigadas (4.0)", command=self.mostrar_brigadas)
        self.btn_brig.grid(row=4, column=0, padx=20, pady=10)

        self.btn_activ = ctk.CTkButton(self.sidebar, text="Actividades (5.0)", command=self.mostrar_actividades)
        self.btn_activ.grid(row=5, column=0, padx=20, pady=10)

        self.btn_salir = ctk.CTkButton(self.sidebar, text="Salir (9.0)", fg_color="#e74c3c", hover_color="#c0392b", command=self.salir)
        self.btn_salir.grid(row=9, column=0, padx=20, pady=20)

    def limpiar_panel(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ==========================================
    # 1.0 DASHBOARD (Pantalla de Inicio)
    # ==========================================
    def mostrar_dashboard(self):
        self.limpiar_panel()
        
        titulo = ctk.CTkLabel(self.main_frame, text="Panel de Estadísticas Generales", font=("Arial", 26, "bold"))
        titulo.pack(pady=20)
        
        # Contenedor de tarjetas
        info_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        info_frame.pack(pady=10, fill="x", padx=20)
        
        # Tarjeta 1
        card1 = ctk.CTkFrame(info_frame, height=150, fg_color="white")
        card1.pack(side="left", fill="both", expand=True, padx=10)
        ctk.CTkLabel(card1, text="Total Brigadas", font=("Arial", 14)).pack(pady=(20,5))
        ctk.CTkLabel(card1, text="12", font=("Arial", 40, "bold"), text_color="#2980b9").pack(pady=10)
        
        # Tarjeta 2
        card2 = ctk.CTkFrame(info_frame, height=150, fg_color="white")
        card2.pack(side="left", fill="both", expand=True, padx=10)
        ctk.CTkLabel(card2, text="Actividades Pendientes", font=("Arial", 14)).pack(pady=(20,5))
        ctk.CTkLabel(card2, text="5", font=("Arial", 40, "bold"), text_color="#e67e22").pack(pady=10)

    # ==========================================
    # 2.0 MÓDULO INSTITUCIONES
    # ==========================================
    def menu_instituciones(self):
        """Pantalla con Grilla 2x2 de Opciones"""
        self.limpiar_panel()

        titulo = ctk.CTkLabel(self.main_frame, text="Gestión de Instituciones (2.0)", font=("Arial", 24, "bold"))
        titulo.pack(pady=(10, 30))

        # Frame para la grilla 2x2
        grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid_frame.pack(expand=True)

        # Botón 1: Registrar
        btn_reg = ctk.CTkButton(grid_frame, text="REGISTRAR\nNueva Institución", width=200, height=100,
                                font=("Arial", 16, "bold"), command=self.form_inst_registrar)
        btn_reg.grid(row=0, column=0, padx=20, pady=20)

        # Botón 2: Modificar
        btn_mod = ctk.CTkButton(grid_frame, text="MODIFICAR\nDatos Existentes", width=200, height=100,
                                font=("Arial", 16, "bold"), fg_color="#f39c12", hover_color="#d35400",
                                command=self.form_inst_modificar)
        btn_mod.grid(row=0, column=1, padx=20, pady=20)

        # Botón 3: Consultar
        btn_con = ctk.CTkButton(grid_frame, text="CONSULTAR\nListado General", width=200, height=100,
                                font=("Arial", 16, "bold"), fg_color="#27ae60", hover_color="#2ecc71",
                                command=self.form_inst_consultar)
        btn_con.grid(row=1, column=0, padx=20, pady=20)

        # Botón 4: Eliminar
        btn_eli = ctk.CTkButton(grid_frame, text="ELIMINAR\nInstitución", width=200, height=100,
                                font=("Arial", 16, "bold"), fg_color="#c0392b", hover_color="#e74c3c",
                                command=self.form_inst_eliminar)
        btn_eli.grid(row=1, column=1, padx=20, pady=20)

    # --- 2.1 Formulario REGISTRAR Institución ---
    def form_inst_registrar(self):
        self.limpiar_panel()
        
        # Cabecera con botón volver
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)
        
        btn_volver = ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones)
        btn_volver.pack(side="left")
        
        ctk.CTkLabel(header_frame, text="Registrar Nueva Institución", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        # Formulario
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(pady=10, padx=40, fill="both", expand=True)

        ctk.CTkLabel(form_frame, text="Nombre de la Institución:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_inst_nombre = ctk.CTkEntry(form_frame, placeholder_text="Ej: U.E. Rafael Belloso Chacín")
        self.entry_inst_nombre.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Dirección Física:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_inst_direccion = ctk.CTkEntry(form_frame, placeholder_text="Ej: Av. Guajira, Zona Norte")
        self.entry_inst_direccion.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Teléfono de Contacto:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_inst_telefono = ctk.CTkEntry(form_frame, placeholder_text="Ej: 0414-1234567")
        self.entry_inst_telefono.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(form_frame, text="Guardar en Base de Datos", height=40, font=("Arial", 14, "bold"), 
                      command=self.guardar_institucion_mock).pack(pady=30)

    # --- 2.2 Formulario MODIFICAR Institución ---
    def form_inst_modificar(self):
        self.limpiar_panel()
        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Institución", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        
        # Placeholder del formulario
        ctk.CTkLabel(self.main_frame, text="Aquí iría el buscador para seleccionar la institución a editar", text_color="gray").pack(pady=50)

    # --- 2.3 Formulario CONSULTAR Institución ---
    def form_inst_consultar(self):
        self.limpiar_panel()
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Listado de Instituciones", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        
        ctk.CTkLabel(self.main_frame, text="Aquí se mostrará la Tabla con todas las instituciones", text_color="gray").pack(pady=50)

    # --- 2.4 Formulario ELIMINAR Institución ---
    def form_inst_eliminar(self):
        self.limpiar_panel()
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Institución", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)
        
        ctk.CTkLabel(self.main_frame, text="Cuidado: Zona de eliminación de registros", text_color="gray").pack(pady=50)

    # ==========================================
    # OTROS MÓDULOS (Placeholders)
    # ==========================================
    def mostrar_usuarios(self):
        self.limpiar_panel()
        ctk.CTkLabel(self.main_frame, text="Módulo Usuarios (En construcción)", font=("Arial", 20)).pack(pady=50)

    def mostrar_brigadas(self):
        self.limpiar_panel()
        ctk.CTkLabel(self.main_frame, text="Módulo Brigadas (En construcción)", font=("Arial", 20)).pack(pady=50)

    def mostrar_actividades(self):
        self.limpiar_panel()
        ctk.CTkLabel(self.main_frame, text="Módulo Actividades (En construcción)", font=("Arial", 20)).pack(pady=50)

    # --- LÓGICA MOCK ---
    def guardar_institucion_mock(self):
        nombre = self.entry_inst_nombre.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Institución '{nombre}' guardada correctamente.")
            self.menu_instituciones() # Volver al menú después de guardar
        else:
            messagebox.showwarning("Error", "El campo nombre es obligatorio")

    def salir(self):
        resp = messagebox.askyesno("Salir", "¿Desea cerrar el sistema?")
        if resp:
            self.destroy()

if __name__ == "__main__":
    app = SistemaBrigadasApp()
    app.mainloop()