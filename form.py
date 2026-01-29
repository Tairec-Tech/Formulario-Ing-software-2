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

    # --- 2.2 Formulario MODIFICAR Institución ---
    def form_inst_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Institución", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        ctk.CTkLabel(form_frame, text="Buscar por nombre o ID:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_inst_buscar_mod = ctk.CTkEntry(form_frame, placeholder_text="Ej: U.E. Rafael Belloso Chacín")
        self.entry_inst_buscar_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Buscar Institución", width=180, command=self.buscar_inst_modificar).pack(pady=10)

        ctk.CTkLabel(form_frame, text="Nombre de la Institución:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_inst_nombre_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombre actualizado")
        self.entry_inst_nombre_mod.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Dirección Física:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_inst_direccion_mod = ctk.CTkEntry(form_frame, placeholder_text="Nueva dirección")
        self.entry_inst_direccion_mod.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Teléfono de Contacto:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_inst_telefono_mod = ctk.CTkEntry(form_frame, placeholder_text="Nuevo teléfono")
        self.entry_inst_telefono_mod.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(form_frame, text="Guardar Cambios", height=40, font=("Arial", 14, "bold"),
                      fg_color="#f39c12", hover_color="#d35400", command=self.guardar_inst_modificar).pack(pady=30)

    # --- 2.3 Formulario CONSULTAR Instituciones ---
    def form_inst_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Listado de Instituciones", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        tabla_frame = ctk.CTkScrollableFrame(self.main_frame)
        tabla_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        tabla_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Encabezados
        ctk.CTkLabel(tabla_frame, text="Nombre", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Dirección", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Teléfono", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Datos de ejemplo
        datos_ejemplo = [
            ("U.E. Rafael Belloso Chacín", "Av. Guajira, Zona Norte", "0414-1234567"),
            ("Liceo Bolivariano Libertador", "Calle 72 con Av. 5 de Julio", "0261-7654321"),
            ("Escuela Básica Maracaibo", "Sector Santa Rosa", "0424-1112233"),
        ]
        for i, (nombre, direccion, telefono) in enumerate(datos_ejemplo, start=1):
            ctk.CTkLabel(tabla_frame, text=nombre).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=direccion).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=telefono).grid(row=i, column=2, padx=10, pady=5, sticky="w")

    # --- 2.4 Formulario ELIMINAR Institución ---
    def form_inst_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_instituciones).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Institución", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)

        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        ctk.CTkLabel(form_frame, text="Nombre o ID de la institución a eliminar:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_inst_eliminar = ctk.CTkEntry(form_frame, placeholder_text="Ej: U.E. Rafael Belloso Chacín")
        self.entry_inst_eliminar.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(form_frame, text="Esta acción no se puede deshacer.", text_color="gray").pack(pady=10)
        ctk.CTkButton(form_frame, text="Eliminar Institución", height=40, font=("Arial", 14, "bold"),
                      fg_color="#c0392b", hover_color="#e74c3c", command=self.eliminar_inst_mock).pack(pady=30)

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

    # --- 3.2 Formulario MODIFICAR Usuario ---
    def form_usu_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Usuario", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        form_frame = ctk.CTkScrollableFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        ctk.CTkLabel(form_frame, text="Buscar por correo o nombre:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_buscar_mod = ctk.CTkEntry(form_frame, placeholder_text="Ej: usuario@brigadas.com")
        self.entry_usu_buscar_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Buscar Usuario", width=180, fg_color="#f39c12", hover_color="#d35400",
                      command=self.buscar_usu_modificar).pack(pady=10)

        ctk.CTkLabel(form_frame, text="Nombres:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_nombre_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombres")
        self.entry_usu_nombre_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Apellidos:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_apellido_mod = ctk.CTkEntry(form_frame, placeholder_text="Apellidos")
        self.entry_usu_apellido_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Correo Electrónico:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_correo_mod = ctk.CTkEntry(form_frame, placeholder_text="Correo")
        self.entry_usu_correo_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Teléfono:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.entry_usu_telefono_mod = ctk.CTkEntry(form_frame, placeholder_text="Teléfono")
        self.entry_usu_telefono_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Rol en el Sistema:", anchor="w").pack(fill="x", padx=20, pady=(10, 2))
        self.combo_usu_rol_mod = ctk.CTkComboBox(form_frame, values=["Brigadista", "Profesor", "Coordinador", "Administrador"])
        self.combo_usu_rol_mod.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(form_frame, text="Guardar Cambios", height=40, font=("Arial", 14, "bold"),
                      fg_color="#f39c12", hover_color="#d35400", command=self.guardar_usu_modificar).pack(pady=30)

    # --- 3.3 Formulario CONSULTAR Usuarios ---
    def form_usu_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(header_frame, text="Directorio de Usuarios", font=("Arial", 20, "bold")).pack(side="left", padx=20)

        tabla_frame = ctk.CTkScrollableFrame(self.main_frame)
        tabla_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        tabla_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        ctk.CTkLabel(tabla_frame, text="Nombre", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Correo", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Teléfono", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Rol", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10, pady=10, sticky="w")

        datos_usuarios = [
            ("Juan Pérez", "juan@brigadas.com", "0412-1234567", "Brigadista"),
            ("María Rodríguez", "maria@brigadas.com", "0414-7654321", "Coordinador"),
            ("Carlos Gómez", "carlos@brigadas.com", "0424-1112233", "Profesor"),
        ]
        for i, (nombre, correo, tel, rol) in enumerate(datos_usuarios, start=1):
            ctk.CTkLabel(tabla_frame, text=nombre).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=correo).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=tel).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=rol).grid(row=i, column=3, padx=10, pady=5, sticky="w")

    # --- 3.4 Formulario ELIMINAR Usuario ---
    def form_usu_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.menu_usuarios).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Usuario", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)

        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)

        ctk.CTkLabel(form_frame, text="Correo o nombre del usuario a eliminar:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_usu_eliminar = ctk.CTkEntry(form_frame, placeholder_text="Ej: usuario@brigadas.com")
        self.entry_usu_eliminar.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Esta acción no se puede deshacer.", text_color="gray").pack(pady=10)
        ctk.CTkButton(form_frame, text="Eliminar Usuario", height=40, font=("Arial", 14, "bold"),
                      fg_color="#c0392b", hover_color="#e74c3c", command=self.eliminar_usu_mock).pack(pady=30)

    # ==========================================
    # 4.0 MÓDULO BRIGADAS
    # ==========================================
    def mostrar_brigadas(self):
        self.limpiar_panel()
        grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid_frame.grid(row=0, column=0, sticky="nsew")
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(0, weight=0)
        grid_frame.grid_rowconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(2, weight=1)

        titulo = ctk.CTkLabel(grid_frame, text="Gestión de Brigadas (4.0)", font=("Arial", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 30))

        btn_reg = ctk.CTkButton(grid_frame, text="REGISTRAR\nNueva Brigada", font=("Arial", 16, "bold"), command=self.form_brig_registrar)
        btn_reg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        btn_mod = ctk.CTkButton(grid_frame, text="MODIFICAR\nBrigada", font=("Arial", 16, "bold"), fg_color="#f39c12", hover_color="#d35400", command=self.form_brig_modificar)
        btn_mod.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        btn_con = ctk.CTkButton(grid_frame, text="CONSULTAR\nListado de Brigadas", font=("Arial", 16, "bold"), fg_color="#27ae60", hover_color="#2ecc71", command=self.form_brig_consultar)
        btn_con.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        btn_eli = ctk.CTkButton(grid_frame, text="ELIMINAR\nBrigada", font=("Arial", 16, "bold"), fg_color="#c0392b", hover_color="#e74c3c", command=self.form_brig_eliminar)
        btn_eli.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    def form_brig_registrar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_brigadas).pack(side="left")
        ctk.CTkLabel(header_frame, text="Registrar Nueva Brigada", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Nombre de la Brigada:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_brig_nombre = ctk.CTkEntry(form_frame, placeholder_text="Ej: Brigada Ecológica Norte")
        self.entry_brig_nombre.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Institución:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_brig_institucion = ctk.CTkEntry(form_frame, placeholder_text="Ej: U.E. Rafael Belloso Chacín")
        self.entry_brig_institucion.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Coordinador:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_brig_coordinador = ctk.CTkEntry(form_frame, placeholder_text="Nombre del coordinador")
        self.entry_brig_coordinador.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Descripción / Objetivo:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_brig_desc = ctk.CTkEntry(form_frame, placeholder_text="Breve descripción de la brigada")
        self.entry_brig_desc.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Guardar Brigada", height=40, font=("Arial", 14, "bold"), command=self.guardar_brigada_mock).pack(pady=30)

    def form_brig_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_brigadas).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Brigada", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Buscar por nombre:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_brig_buscar_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombre de la brigada")
        self.entry_brig_buscar_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Buscar", width=180, fg_color="#f39c12", hover_color="#d35400", command=self.buscar_brig_modificar).pack(pady=10)
        ctk.CTkLabel(form_frame, text="Nombre:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_brig_nombre_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombre")
        self.entry_brig_nombre_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Coordinador:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_brig_coordinador_mod = ctk.CTkEntry(form_frame, placeholder_text="Coordinador")
        self.entry_brig_coordinador_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Guardar Cambios", height=40, font=("Arial", 14, "bold"), fg_color="#f39c12", hover_color="#d35400", command=self.guardar_brig_modificar).pack(pady=30)

    def form_brig_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_brigadas).pack(side="left")
        ctk.CTkLabel(header_frame, text="Listado de Brigadas", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        tabla_frame = ctk.CTkScrollableFrame(self.main_frame)
        tabla_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        tabla_frame.grid_columnconfigure((0, 1, 2), weight=1)
        ctk.CTkLabel(tabla_frame, text="Brigada", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Institución", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Coordinador", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        datos_brig = [("Brigada Ecológica Norte", "U.E. Rafael Belloso Chacín", "María Rodríguez"), ("Brigada de Reciclaje", "Liceo Libertador", "Carlos Gómez")]
        for i, (brig, inst, coord) in enumerate(datos_brig, start=1):
            ctk.CTkLabel(tabla_frame, text=brig).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=inst).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=coord).grid(row=i, column=2, padx=10, pady=5, sticky="w")

    def form_brig_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_brigadas).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Brigada", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Nombre de la brigada a eliminar:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_brig_eliminar = ctk.CTkEntry(form_frame, placeholder_text="Nombre de la brigada")
        self.entry_brig_eliminar.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Esta acción no se puede deshacer.", text_color="gray").pack(pady=10)
        ctk.CTkButton(form_frame, text="Eliminar Brigada", height=40, font=("Arial", 14, "bold"), fg_color="#c0392b", hover_color="#e74c3c", command=self.eliminar_brig_mock).pack(pady=30)

    # ==========================================
    # 5.0 MÓDULO ACTIVIDADES
    # ==========================================
    def mostrar_actividades(self):
        self.limpiar_panel()
        grid_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        grid_frame.grid(row=0, column=0, sticky="nsew")
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(0, weight=0)
        grid_frame.grid_rowconfigure(1, weight=1)
        grid_frame.grid_rowconfigure(2, weight=1)
        titulo = ctk.CTkLabel(grid_frame, text="Gestión de Actividades (5.0)", font=("Arial", 24, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 30))
        btn_reg = ctk.CTkButton(grid_frame, text="REGISTRAR\nNueva Actividad", font=("Arial", 16, "bold"), command=self.form_activ_registrar)
        btn_reg.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        btn_mod = ctk.CTkButton(grid_frame, text="MODIFICAR\nActividad", font=("Arial", 16, "bold"), fg_color="#f39c12", hover_color="#d35400", command=self.form_activ_modificar)
        btn_mod.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        btn_con = ctk.CTkButton(grid_frame, text="CONSULTAR\nListado de Actividades", font=("Arial", 16, "bold"), fg_color="#27ae60", hover_color="#2ecc71", command=self.form_activ_consultar)
        btn_con.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        btn_eli = ctk.CTkButton(grid_frame, text="ELIMINAR\nActividad", font=("Arial", 16, "bold"), fg_color="#c0392b", hover_color="#e74c3c", command=self.form_activ_eliminar)
        btn_eli.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    def form_activ_registrar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_actividades).pack(side="left")
        ctk.CTkLabel(header_frame, text="Registrar Nueva Actividad", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Nombre de la Actividad:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_activ_nombre = ctk.CTkEntry(form_frame, placeholder_text="Ej: Jornada de Reforestación")
        self.entry_activ_nombre.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Brigada asignada:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_activ_brigada = ctk.CTkEntry(form_frame, placeholder_text="Nombre de la brigada")
        self.entry_activ_brigada.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Fecha:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_activ_fecha = ctk.CTkEntry(form_frame, placeholder_text="DD/MM/AAAA")
        self.entry_activ_fecha.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Tipo:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.combo_activ_tipo = ctk.CTkComboBox(form_frame, values=["Ecológica", "Deportiva", "Cultural", "Social", "Otro"])
        self.combo_activ_tipo.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Descripción:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_activ_desc = ctk.CTkEntry(form_frame, placeholder_text="Breve descripción")
        self.entry_activ_desc.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Guardar Actividad", height=40, font=("Arial", 14, "bold"), command=self.guardar_actividad_mock).pack(pady=30)

    def form_activ_modificar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_actividades).pack(side="left")
        ctk.CTkLabel(header_frame, text="Modificar Actividad", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Buscar por nombre:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_activ_buscar_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombre de la actividad")
        self.entry_activ_buscar_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Buscar", width=180, fg_color="#f39c12", hover_color="#d35400", command=self.buscar_activ_modificar).pack(pady=10)
        ctk.CTkLabel(form_frame, text="Nombre:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_activ_nombre_mod = ctk.CTkEntry(form_frame, placeholder_text="Nombre")
        self.entry_activ_nombre_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Fecha:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.entry_activ_fecha_mod = ctk.CTkEntry(form_frame, placeholder_text="DD/MM/AAAA")
        self.entry_activ_fecha_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Tipo:", anchor="w").pack(fill="x", padx=20, pady=(15, 5))
        self.combo_activ_tipo_mod = ctk.CTkComboBox(form_frame, values=["Ecológica", "Deportiva", "Cultural", "Social", "Otro"])
        self.combo_activ_tipo_mod.pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(form_frame, text="Guardar Cambios", height=40, font=("Arial", 14, "bold"), fg_color="#f39c12", hover_color="#d35400", command=self.guardar_activ_modificar).pack(pady=30)

    def form_activ_consultar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_actividades).pack(side="left")
        ctk.CTkLabel(header_frame, text="Listado de Actividades", font=("Arial", 20, "bold")).pack(side="left", padx=20)
        tabla_frame = ctk.CTkScrollableFrame(self.main_frame)
        tabla_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        tabla_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        ctk.CTkLabel(tabla_frame, text="Actividad", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Brigada", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Fecha", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(tabla_frame, text="Tipo", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10, pady=10, sticky="w")
        datos_activ = [("Jornada de Reforestación", "Brigada Ecológica Norte", "15/02/2025", "Ecológica"), ("Campaña de Reciclaje", "Brigada de Reciclaje", "20/03/2025", "Ecológica")]
        for i, (activ, brig, fecha, tipo) in enumerate(datos_activ, start=1):
            ctk.CTkLabel(tabla_frame, text=activ).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=brig).grid(row=i, column=1, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=fecha).grid(row=i, column=2, padx=10, pady=5, sticky="w")
            ctk.CTkLabel(tabla_frame, text=tipo).grid(row=i, column=3, padx=10, pady=5, sticky="w")

    def form_activ_eliminar(self):
        self.limpiar_panel()
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        ctk.CTkButton(header_frame, text="< Volver", width=60, fg_color="gray", command=self.mostrar_actividades).pack(side="left")
        ctk.CTkLabel(header_frame, text="Eliminar Actividad", font=("Arial", 20, "bold"), text_color="#c0392b").pack(side="left", padx=20)
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=10)
        ctk.CTkLabel(form_frame, text="Nombre de la actividad a eliminar:", anchor="w").pack(fill="x", padx=20, pady=(20, 5))
        self.entry_activ_eliminar = ctk.CTkEntry(form_frame, placeholder_text="Nombre de la actividad")
        self.entry_activ_eliminar.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(form_frame, text="Esta acción no se puede deshacer.", text_color="gray").pack(pady=10)
        ctk.CTkButton(form_frame, text="Eliminar Actividad", height=40, font=("Arial", 14, "bold"), fg_color="#c0392b", hover_color="#e74c3c", command=self.eliminar_activ_mock).pack(pady=30)

    # --- LÓGICA MOCK ---
    def guardar_institucion_mock(self):
        nombre = self.entry_inst_nombre.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Institución '{nombre}' guardada correctamente.")
            self.menu_instituciones()
        else:
            messagebox.showwarning("Error", "El campo nombre es obligatorio")

    def buscar_inst_modificar(self):
        busqueda = self.entry_inst_buscar_mod.get()
        if busqueda:
            self.entry_inst_nombre_mod.insert(0, busqueda)
            self.entry_inst_direccion_mod.insert(0, "Av. Guajira, Zona Norte")
            self.entry_inst_telefono_mod.insert(0, "0414-1234567")
            messagebox.showinfo("Búsqueda", "Datos cargados para edición.")
        else:
            messagebox.showwarning("Error", "Ingrese un nombre o ID para buscar.")

    def guardar_inst_modificar(self):
        nombre = self.entry_inst_nombre_mod.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Institución '{nombre}' actualizada correctamente.")
            self.menu_instituciones()
        else:
            messagebox.showwarning("Error", "El campo nombre es obligatorio.")

    def eliminar_inst_mock(self):
        nombre = self.entry_inst_eliminar.get()
        if nombre:
            if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la institución '{nombre}'?"):
                messagebox.showinfo("Eliminado", f"Institución '{nombre}' ha sido eliminada.")
                self.menu_instituciones()
        else:
            messagebox.showwarning("Error", "Ingrese el nombre o ID de la institución.")

    def guardar_usuario_mock(self):
        nombre = self.entry_usu_nombre.get()
        rol = self.combo_usu_rol.get()
        if nombre:
            messagebox.showinfo("Usuario Registrado", f"El usuario {nombre} ha sido registrado como {rol}.")
            self.menu_usuarios()
        else:
            messagebox.showwarning("Error", "El nombre es obligatorio")

    def buscar_usu_modificar(self):
        busqueda = self.entry_usu_buscar_mod.get()
        if busqueda:
            self.entry_usu_nombre_mod.insert(0, "Juan Antonio")
            self.entry_usu_apellido_mod.insert(0, "Pérez Rodríguez")
            self.entry_usu_correo_mod.insert(0, busqueda if "@" in busqueda else "usuario@brigadas.com")
            self.entry_usu_telefono_mod.insert(0, "0412-1234567")
            self.combo_usu_rol_mod.set("Brigadista")
            messagebox.showinfo("Búsqueda", "Datos cargados para edición.")
        else:
            messagebox.showwarning("Error", "Ingrese correo o nombre para buscar.")

    def guardar_usu_modificar(self):
        nombre = self.entry_usu_nombre_mod.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' actualizado correctamente.")
            self.menu_usuarios()
        else:
            messagebox.showwarning("Error", "El nombre es obligatorio.")

    def eliminar_usu_mock(self):
        dato = self.entry_usu_eliminar.get()
        if dato:
            if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario '{dato}'?"):
                messagebox.showinfo("Eliminado", "Usuario eliminado del sistema.")
                self.menu_usuarios()
        else:
            messagebox.showwarning("Error", "Ingrese correo o nombre del usuario.")

    def guardar_brigada_mock(self):
        nombre = self.entry_brig_nombre.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Brigada '{nombre}' registrada correctamente.")
            self.mostrar_brigadas()
        else:
            messagebox.showwarning("Error", "El nombre de la brigada es obligatorio.")

    def buscar_brig_modificar(self):
        busqueda = self.entry_brig_buscar_mod.get()
        if busqueda:
            self.entry_brig_nombre_mod.insert(0, busqueda)
            self.entry_brig_coordinador_mod.insert(0, "María Rodríguez")
            messagebox.showinfo("Búsqueda", "Datos cargados para edición.")
        else:
            messagebox.showwarning("Error", "Ingrese el nombre de la brigada.")

    def guardar_brig_modificar(self):
        nombre = self.entry_brig_nombre_mod.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Brigada '{nombre}' actualizada correctamente.")
            self.mostrar_brigadas()
        else:
            messagebox.showwarning("Error", "El nombre es obligatorio.")

    def eliminar_brig_mock(self):
        nombre = self.entry_brig_eliminar.get()
        if nombre:
            if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la brigada '{nombre}'?"):
                messagebox.showinfo("Eliminado", f"Brigada '{nombre}' ha sido eliminada.")
                self.mostrar_brigadas()
        else:
            messagebox.showwarning("Error", "Ingrese el nombre de la brigada.")

    def guardar_actividad_mock(self):
        nombre = self.entry_activ_nombre.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Actividad '{nombre}' registrada correctamente.")
            self.mostrar_actividades()
        else:
            messagebox.showwarning("Error", "El nombre de la actividad es obligatorio.")

    def buscar_activ_modificar(self):
        busqueda = self.entry_activ_buscar_mod.get()
        if busqueda:
            self.entry_activ_nombre_mod.insert(0, busqueda)
            self.entry_activ_fecha_mod.insert(0, "15/02/2025")
            self.combo_activ_tipo_mod.set("Ecológica")
            messagebox.showinfo("Búsqueda", "Datos cargados para edición.")
        else:
            messagebox.showwarning("Error", "Ingrese el nombre de la actividad.")

    def guardar_activ_modificar(self):
        nombre = self.entry_activ_nombre_mod.get()
        if nombre:
            messagebox.showinfo("Éxito", f"Actividad '{nombre}' actualizada correctamente.")
            self.mostrar_actividades()
        else:
            messagebox.showwarning("Error", "El nombre es obligatorio.")

    def eliminar_activ_mock(self):
        nombre = self.entry_activ_eliminar.get()
        if nombre:
            if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la actividad '{nombre}'?"):
                messagebox.showinfo("Eliminado", f"Actividad '{nombre}' ha sido eliminada.")
                self.mostrar_actividades()
        else:
            messagebox.showwarning("Error", "Ingrese el nombre de la actividad.")

    def salir(self):
        resp = messagebox.askyesno("Salir", "¿Desea cerrar el sistema?")
        if resp:
            self.destroy()

if __name__ == "__main__":
    app = SistemaBrigadasApp()
    app.mainloop()