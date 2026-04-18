class cliente:
    def __init__(self, nombre, apellido, genero, ocupacacion):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__ocupacacion = ocupacacion
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def get_genero(self):
        return self.__genero
    def get_ocupacion(self):
        return self.__ocupacacion
    def set_ocupacion(self, ocupacion):
        self.__ocupacion = ocupacion

cliente1 = cliente("Escarlet", "Gaunt", "Femenino", "Estudiante")
print(cliente1.get_nombre())
print(cliente1.get_apellido())
print(cliente1.get_genero())
print(cliente1.get_ocupacion())
