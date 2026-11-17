class Pokemon:
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = int(id)
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(velocidad)
        self.generacion = int(generacion)

    def __str__(self):
        if self.tipo2:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def __eq__(self, otro):
        if isinstance(otro, Pokemon):
            return self.id == otro.id
        return False

# TEORIA
# La identidad es el atributo id y el estado son los demás atributos, y no, la identidad no debería poder cambiar nunca.