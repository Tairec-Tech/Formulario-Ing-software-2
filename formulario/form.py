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
        self.geometry("1100x700")

        # Layout Principal: 2 Columnas
        self.grid_columnconfigure(1, weight=1) # La columna de contenido se expande
        self.grid_rowconfigure(0, weight=1)    # La fila se expande

        # 2. Crear Menú Lateral
        self.crear_menu_lateral()

        # 3. Frame Principal (Área de trabajo)
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Configuración inicial de expansión para el main_frame
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

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
        self.btn_inst = ctk.CTkButton(self.sidebar, text="Instituciones (2.0)", command=self.menu_instituciones)
        self.btn_inst.grid(row=2, column=0, padx=20, pady=10)

        self.btn_usu = ctk.CTkButton(self.sidebar, text="Usuarios (3.0)", command=self.menu_usuarios)
        self.btn_usu.grid(row=3, column=0, padx=20, pady=10)

        self.btn_brig = ctk.CTkButton(self.sidebar, text="Brigadas (4.0)", command=self.mostrar_brigadas)
        self.btn_brig.grid(row=4, column=0, padx=20, pady=10)

        self.btn_activ = ctk.CTkButton(self.sidebar, text="Actividades (5.0)", command=self.mostrar_actividades)
        self.btn_activ.grid(row=5, column=0, padx=20, pady=10)

        self.btn_salir = ctk.CTkButton(self.sidebar, text="Salir (9.0)", fg_color="#e74c3c", hover_color="#c0392b", command=self.salir)
        self.btn_salir.grid(row=9, column=0, padx=20, pady=20)

    def limpiar_panel(self):
        """Elimina widgets y resetea la configuración del grid"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Resetear configuración por defecto (Fila 0 expandible)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0) 
        self.main_frame.grid_columnconfigure(0, weight=1)

    # ==========================================
    # 1.0 DASHBOARD (Pantalla de Inicio)
    # ==========================================
    def mostrar_dashboard(self):
        self.limpiar_panel()
        
        # Frame contenedor que se expande
        content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        content_frame.grid(row=0, column=0, sticky="nsew")
        content_frame.grid_columnconfigure((0, 1), weight=1)
        
        titulo = ctk.CTkLabel(content_frame, text="Panel de Estadísticas Generales", font=("Arial", 26, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Tarjeta 1
        card1 = ctk.CTkFrame(content_frame, height=150, fg_color="white")
        card1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        ctk.CTkLabel(card1, text="Total Brigadas", font=("Arial", 14)).pack(pady=(20,5))
        ctk.CTkLabel(card1, text="12", font=("Arial", 40, "bold"), text_color="#2980b9").pack(pady=10)
        
        # Tarjeta 2
        card2 = ctk.CTkFrame(content_frame, height=150, fg_color="white")
        card2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        ctk.CTkLabel(card2, text="Actividades Pendientes", font=("Arial", 14)).pack(pady=(20,5))
        ctk.CTkLabel(card2, text="5", font=("Arial", 40, "bold"), text_color="#e67e22").pack(pady=10)

    # ==========================================
    # 2.0 MÓDULO INSTITUCIONES
    # ==========================================
    def menu_instituciones(self):
        self.limpiar_panel()
        # Aquí usamos Fila 0 con Weight 1 (Configuración por defecto de limpiar_panel)

        grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid_frame.grid(row=0, column=0, sticky="nsew")
        
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(0, weight=0) # Título fijo
        grid_frame.grid_rowconfigure(1, weight=1) # Botones expandibles
        grid_frame.grid_rowconfigure(2, weight=1) # Botones expandibles

        titulo = ctk.CTkLabel(grid_frame, text="Gestión de Instituciones (2.0)", font=("Arial", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 30))

        btn_reg = ctk.CTkButton(grid_frame, text="REGISTRAR\nNueva Institución",
                                font=("Arial", 16, "bold"), command=self.form_inst_registrar)
        btn_reg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        btn_mod = ctk.CTkButton(grid_frame, text="MODIFICAR\nDatos Existentes",
                                font=("Arial", 16, "bold"), fg_color="#f39c12", hover_color="#d35400",
                                command=self.form_inst_modificar)
        btn_mod.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        btn_con = ctk.CTkButton(grid_frame, text="CONSULTAR\nListado General",
                                font=("Arial", 16, "bold"), fg_color="#27ae60", hover_color="#2ecc71",
                                command=self.form_inst_consultar)
        btn_con.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        btn_eli = ctk.CTkButton(grid_frame, text="ELIMINAR\nInstitución",
                                font=("Arial", 16, "bold"), fg_color="#c0392b", hover_color="#e74c3c",
                                command=self.form_inst_eliminar)
        btn_eli.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    # --- 2.1 Formulario REGISTRAR Institución ---
    def form_inst_registrar(self):
        self.limpiar_panel()
        
        # CORRECCIÓN DE EXPANSIÓN:
        # Fila 0 (Header) = Weight 0 (Fijo)
        # Fila 1 (Formulario) = Weight 1 (Expande)
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        btn_volver = ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones)
        btn_volver.pack(side="left")
        
        ctk.CTkLabel(header_frame, text="Registrar Nueva Institución", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        # Formulario
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

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

    # --- Placeholders 2.x ---
    def form_inst_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Institución", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        
        ctk.CTkLabel(self.main_frame, text="Aquí iría el buscador...", text_color="gray").grid(row=1, column=0)

    def form_inst_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Listado de Instituciones", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        
        ctk.CTkLabel(self.main_frame, text="Tabla de Consulta", text_color="gray").grid(row=1, column=0)

    def form_inst_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Institución", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)
        
        ctk.CTkLabel(self.main_frame, text="Zona de Eliminación", text_color="gray").grid(row=1, column=0)

    # ==========================================
    # 3.0 MÓDULO USUARIOS
    # ==========================================
    def menu_usuarios(self):
        self.limpiar_panel()
        # Fila 0 expande (por defecto)

        grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid_frame.grid(row=0, column=0, sticky="nsew")
        
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(0, weight=0) 
        grid_frame.grid_rowconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(2, weight=1) 

        titulo = ctk.CTkLabel(grid_frame, text="Gestión de Usuarios (3.0)", font=("Arial", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 30))

        btn_reg = ctk.CTkButton(grid_frame, text="REGISTRAR\nNuevo Usuario",
                                font=("Arial", 16, "bold"), command=self.form_usu_registrar)
        btn_reg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        btn_mod = ctk.CTkButton(grid_frame, text="MODIFICAR\nUsuario",
                                font=("Arial", 16, "bold"), fg_color="#f39c12", hover_color="#d35400",
                                command=self.form_usu_modificar)
        btn_mod.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        btn_con = ctk.CTkButton(grid_frame, text="CONSULTAR\nDirectorio de Usuarios",
                                font=("Arial", 16, "bold"), fg_color="#27ae60", hover_color="#2ecc71",
                                command=self.form_usu_consultar)
        btn_con.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        btn_eli = ctk.CTkButton(grid_frame, text="ELIMINAR\nUsuario",
                                font=("Arial", 16, "bold"), fg_color="#c0392b", hover_color="#e74c3c",
                                command=self.form_usu_eliminar)
        btn_eli.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    # --- 3.1 Formulario REGISTRAR Usuario ---
    def form_usu_registrar(self):
        self.limpiar_panel()
        # CORRECCIÓN DE EXPANSIÓN
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        btn_volver = ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios)
        btn_volver.pack(side="left")
        
        ctk.CTkLabel(header_frame, text="Registrar Nuevo Usuario", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        form_frame = ctk.CTkScrollableFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        # Campos
        ctk.CTkLabel(form_frame, text="Nombres:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_nombre = ctk.CTkEntry(form_frame, placeholder_text="Ej: Juan Antonio")
        self.entry_usu_nombre.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Apellidos:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_apellido = ctk.CTkEntry(form_frame, placeholder_text="Ej: Pérez Rodríguez")
        self.entry_usu_apellido.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Correo Electrónico:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_correo = ctk.CTkEntry(form_frame, placeholder_text="Ej: usuario@brigadas.com")
        self.entry_usu_correo.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Teléfono:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_telefono = ctk.CTkEntry(form_frame, placeholder_text="Ej: 0412-1234567")
        self.entry_usu_telefono.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Dirección de Habitación:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_direccion = ctk.CTkEntry(form_frame, placeholder_text="Sector, Calle, Nº de Casa")
        self.entry_usu_direccion.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Rol en el Sistema:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.combo_usu_rol = ctk.CTkComboBox(form_frame, values=["Brigadista", "Profesor", "Coordinador", "Administrador"])
        self.combo_usu_rol.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(form_frame, text="Registrar Usuario", height=40, font=("Arial", 14, "bold"), 
                      command=self.guardar_usuario_mock).pack(pady=30)

    # --- Placeholders 3.x ---
    def form_usu_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(self.main_frame, text="Modificar Usuario", text_color="gray").grid(row=1, column=0)

    def form_usu_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(self.main_frame, text="Tabla Usuarios", text_color="gray").grid(row=1, column=0)

    def form_usu_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(self.main_frame, text="Eliminar Usuario", text_color="red").grid(row=1, column=0)

    # ==========================================
    # OTROS MÓDULOS (Placeholders)
    # ==========================================
    def mostrar_brigadas(self):
        self.limpiar_panel()
        ctk.CTkLabel(self.main_frame, text="Módulo Brigadas (En construcción)", font=("Arial", 20)).grid(row=0, column=0)

    def mostrar_actividades(self):
        self.limpiar_panel()
        ctk.CTkLabel(self.main_frame, text="Módulo Actividades (En construcción)", font=("Arial", 20)).grid(row=0, column=0)

    # --- LÓGICA MOCK ---
    def guardar_institucion_mock(self):
        nombre = self.entry_inst_nombre.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Institución '{nombre}' guardada correctamente.")
            self.menu_instituciones()
        else:
            messagebox.showwarning("Error", "El campo nombre es obligatorio")

    def guardar_usuario_mock(self):
        nombre = self.entry_usu_nombre.get()
        rol = self.combo_usu_rol.get()
        if nombre:
            messagebox.showinfo("Usuario Registrado", f"El usuario {nombre} ha sido registrado como {rol}.")
            self.menu_usuarios()
        else:
            messagebox.showwarning("Error", "El nombre es obligatorio")

    def salir(self):
        resp = messagebox.askyesno("Salir", "¿Desea cerrar el sistema?")
        if resp:
            self.destroy()

if __name__ == "__main__":
    app = SistemaBrigadasApp()
    app.mainloop()