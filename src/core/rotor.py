from string import ascii_lowercase
from core.builder import BaseBuilder


class Rotor:
    def __init__(
        self,
        name: str,
        wiring: str,
        ring="a",
        notchs: str = ""
    ) -> None:
        self.name = name
        self.wiring = wiring
        self.ring = ring
        self.notchs = notchs

    @property
    def is_in_turnover_pos(self):
        if self.ring in self.notchs:
            return True
        return False

    def encipher_right(self, symbol: str, previus_rotor_ring: str = None) -> str:
        if previus_rotor_ring is None:
            previus_rotor_ring = "a"
        shift = (ascii_lowercase.find(symbol) + (ascii_lowercase.find(self.ring) - ascii_lowercase.find(previus_rotor_ring))) % 26
        return self.wiring[shift]

    def encipher_left(self, symbol: str, next_rotor_ring: str = None) -> str:
        if next_rotor_ring:
            a = (ascii_lowercase.find(next_rotor_ring) - ascii_lowercase.find(self.ring)) % 26
            shift = (ascii_lowercase.find(symbol) - a) % 26
        else:
            shift = (ascii_lowercase.find(symbol) + ascii_lowercase.find(self.ring)) % 26
        return ascii_lowercase[self.wiring.find(ascii_lowercase[shift])]

    def turn(self) -> bool:
        self.ring = (
            chr(ord(self.ring) + 1)
            if ord(self.ring) + 1 <= 122
            else "a"
        )
        return self.is_in_turnover_pos


class RotorBuilder(BaseBuilder[Rotor]):
    ...


rotorb_instance = RotorBuilder()

rotorb_instance.register(
    Rotor(
        name="I",
        wiring="ekmflgdqvzntowyhxuspaibrcj",
        notchs="r"
    ), "ROTOR_I"
)
rotorb_instance.register(
    Rotor(
        name="II",
        wiring="ajdksiruxblhwtmcqgznpyfvoe",
        notchs="r"
    ), "ROTOR_II"
)
rotorb_instance.register(
    Rotor(
        name="III",
        wiring="bdfhjlcprtxvznyeiwgakmusqo",
        notchs="r"
    ), "ROTOR_III"
)
rotorb_instance.register(
    Rotor(
        name="IV",
        wiring="esovpzjayquirhxlnftgkdcmwb",
        notchs="k"
    ), "ROTOR_IV"
)
rotorb_instance.register(
    Rotor(
        name="V",
        wiring="vzbrgityupsdnhlxawmjqofeck",
        notchs="a"
    ), "ROTOR_V"
)
rotorb_instance.register(
    Rotor(
        name="ETW",
        wiring=ascii_lowercase,
        notchs="r",
    ), "ROTOR_ETW"
)
