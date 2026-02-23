class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def aplicar_aumento(self, porcentaje):
        """aumenta el salario segun un porcentaje"""
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
    def mostrar_informacion(self):
        """muestra la informacion del empleado"""
        print(f"nombre: {self.nombre}")
        print(f"cargo: {self.cargo}")
        print(f"salario: ${self.salario:.2f}")
        print("-" * 30)
class GestionEmpleados:
    def __init__(self):
        self.lista_empleados = []
    def agregar_empleado(self, empleado):
        self.lista_empleados.append(empleado)
    def calcular_salarios_totales(self):
        total = 0
        for empleado in self.lista_empleados:
            total += empleado.salario
        return total
    def aplicar_aumento_general(self, porcentaje):
        for empleado in self.lista_empleados:
            empleado.aplicar_aumento(porcentaje)
    def mostrar_empleados(self):
        for empleado in self.lista_empleados:
            empleado.mostrar_informacion()
gestion = GestionEmpleados()
emp1 = Empleado("ana", "desarrolladora", 3000)
emp2 = Empleado("carlos", "diseñador", 2500)
emp3 = Empleado("maría", "gerente", 4000)
gestion.agregar_empleado(emp1)
gestion.agregar_empleado(emp2)
gestion.agregar_empleado(emp3)
print("lista de empleados:")
gestion.mostrar_empleados()
total = gestion.calcular_salarios_totales()
print(f"total de salarios: ${total:.2f}")
print("\n aplicando aumento del 10%...")
gestion.aplicar_aumento_general(10)
print("\nlista actualizada:")
gestion.mostrar_empleados()
nuevo_total = gestion.calcular_salarios_totales()
print(f"nuevo total de salarios: ${nuevo_total:.2f}")