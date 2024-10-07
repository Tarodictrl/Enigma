from string import ascii_lowercase

from core.builder import BaseBuilder


class Reflector:

    def __init__(self, name: str, wiring: str) -> None:
        self.name = name
        self.wiring = wiring

    def encipher(self, symbol: str, previus_rotor_ring: str = "a") -> str:
        shift = (ascii_lowercase.find(symbol) - ascii_lowercase.find(previus_rotor_ring)) % 26
        return self.wiring[shift]


class ReflectorBuilder(BaseBuilder[Reflector]):
    ...


reflectorb_instance = ReflectorBuilder()

reflectorb_instance.register(
    Reflector(
        name="Reflector UKW-A",
        wiring="ejmzalyxvbwfcrquontspikhgd"
    ),
    "UKW_A"
)
reflectorb_instance.register(
    Reflector(
        name="Reflector UKW-B",
        wiring="yruhqsldpxngokmiebfzcwvjat"
    ),
    "UKW_B"
)
reflectorb_instance.register(
    Reflector(
        name="Reflector UKW-C",
        wiring="fvpjiaoyedrzxwgctkuqsbnmhl"
    ),
    "UKW_C"
)
