from Ejercicio_01 import Pokemon

class PokemonNoEncontrado(Exception):
    pass

class Pokedex:
    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        for i, p in enumerate(self.pokemones):
            if p.id == pokemon.id:
                self.pokemones[i] = pokemon
                return
        self.pokemones.append(pokemon)

    def obtener(self, id):
        for p in self.pokemones:
            if p.id == id:
                return p
        raise PokemonNoEncontrado(f"No existe un Pokémon con id {id}.")

    def listar(self):
        return list(self.pokemones)

    def cantidad(self):
        return len(self.pokemones)

# TEORIA
# Al lanzar una excepción, el método fuerza a quien lo llama a manejar el error en el momento,
# evitando que el programa arrastre un valor nulo (None) que genere fallos inesperados más adelante.