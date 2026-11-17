from Ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self.items = ListaEnlazada()

    def encolar(self, dato):
        self.items.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.items.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self.items.primero.dato

    def esta_vacia(self):
        return self.items.esta_vacia()

class ColaTurnos:
    def __init__(self):
        self.turnos = Cola()

    def encolar(self, pokemon):
        self.turnos.encolar(pokemon)

    def siguiente(self):
        return self.turnos.desencolar()

    def proximo(self):
        return self.turnos.ver_frente()

# TEORIA
# No devuelve C porque las colas operan bajo la política FIFO (First in, First Out). Como A fue el primer elemento en ingresar, es el primero que debe salir.