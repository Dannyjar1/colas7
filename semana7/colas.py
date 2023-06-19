from collections import deque

class Consulta:
    def __init__(self, nombre, correo, mensaje):
        self.nombre = nombre
        self.correo = correo
        self.mensaje = mensaje
    
    def __str__(self):
        return f"Consulta{{nombre={self.nombre}, correo={self.correo}, mensaje={self.mensaje}}}"

class GestorConsultas:
    def __init__(self):
        self.cola = deque()
    
    def nuevaConsulta(self, c):
        self.cola.append(c)
        
    def atenderConsulta(self):
        if self.cola:
            print(str(self.cola[0]))
            self.cola.popleft()
        
    def consultasPendientes(self):
        return len(self.cola)

gestor = GestorConsultas()
for _ in range(5):
    print("Ingresa tu nombre:")
    nombre = input()
    print("Ingresa tu correo:")
    correo = input()
    print("Ingresa el motivo de tu consulta:")
    consulta = input()
    gestor.nuevaConsulta(Consulta(nombre, correo, consulta))

print(f"Existen: {gestor.consultasPendientes()} consultas pendientes")
while gestor.consultasPendientes() > 0:
    print("Si desea atender a la consulta, presione 1:")
    bandera = input()
    if bandera == "1":
        gestor.atenderConsulta()
        print(f"Existen: {gestor.consultasPendientes()} consultas pendientes")
