from datetime import date, datetime

class Rol:
    def __init__(self, salario, tiempo, modelo_rol):
        self.salario = salario
        self.tiempo = tiempo
        self.modelo_rol = modelo_rol

    def mostrar_rol(self):
        print("Rol: ",self.modelo_rol,"\ntiempo: ",self.tiempo,"\nsalario: " ,self.salario)

class Usuario(Rol):
    def __init__(self,salario,tiempo,modelo_rol,nombre,apellido,cedula,celular,email):
        super().__init__(salario,tiempo,modelo_rol)
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.celular = celular
        self.email = email
        
    def mostrar_usuario(self):
        print("\nnombre: ",self.nombre,"\napellido: ",self.apellido,"\ncedula: ",self.cedula,"\ncelular: ",self.celular,"\nemail: ",self.email,"\nRol: ",self.modelo_rol)

class Opciones_Sis(Usuario):
    def __init__(self,salario,tiempo,modelo_rol,nombre,apellido,cedula,celular,email,nom_opcion,desarrollo_etapa):
        super().__init__(salario,tiempo,modelo_rol, nombre, apellido,cedula, celular ,email)
        self.nom_opcion = nom_opcion
        self.desarrollo_etapa = desarrollo_etapa

    def mostrar_opciones(self):
        print("\nopción: ",self.nom_opcion,"\nacción: ",self.desarrollo_etapa,"\nRol: ",self.modelo_rol)

class Operaciones:
    def __init__(self,nom_operaciones,tiempo_empleado,operaciones_desarrolladas):
        self.nom_operaciones = nom_operaciones
        self.tiempo_empleado = tiempo_empleado
        self.operaciones_desarrolladas = operaciones_desarrolladas

    def mostrar_operaciones(self):
        print("\noperación: ",self.nom_operaciones,"\ntiempo_empleado: ", self.tiempo_empleado,"\noperaciones_desarrolladas: ", self.operaciones_desarrolladas)

class Modulo_Seguridad:
    def id_modelo(self):
        pass

rol = Rol(456,datetime.today(),"Gerente")
rol.mostrar_rol()

user = Usuario(456,datetime.today,"Gerente"," Carlos ", "0924924677", "0930579345", "cwilsonm")
user.mostrar_usuario()

opciones = Opciones_Sis(456,date.today,"Gerente"," Angel ", "0936947924", "0968935891", "tzuñigap","Admin","Controlar")
opciones.mostrar_opciones()

operacion = Operaciones("Supervisar a sus subordinados",15,25)
operacion.mostrar_operaciones()
