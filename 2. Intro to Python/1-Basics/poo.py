class Persona:
    def __init__(self, nombre, edad):
        """The __init__ is the constructor method similar to the 
        constructors in other OOP languages. It executes immediately 
        when we create an object for the class. It’s used to initialize 
        the initial data for the instance

        Args:
            nombre (string): nombre de la persona
            edad (string): edad de la persona
        """
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_años(self):
        self.edad = self.edad + 1
        print(f"Hola, soy {self.nombre} y hoy cumplo {self.edad} años.")

# Crear objeto de la clase Persona
persona1 = Persona("Juan", 30)

# Llamar al método "saludar" de cada objeto
persona1.saludar()
persona1.cumplir_años()

# persona2.saludar()
