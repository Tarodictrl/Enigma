from string import ascii_lowercase

from core.rotor import Rotor
from core.reflector import Reflector


class Enigma:
    def __init__(
        self,
        plugboard: list[str],
        rotors: list[Rotor],
        reflector: Reflector,
        keys: str = "AAA"
    ) -> None:
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        for rotor, key in zip(self.rotors, keys):
            rotor.ring = key.lower()

    def press(self, symbol: str) -> str:
        self.__turn_rotor(index=len(self.rotors) - 1)
        symbol = symbol.lower()

        symbol = self.__encrypt_plugboard(symbol)
        symbol = self.__encrypt_by_rotors_right(symbol)
        symbol = self.reflector.encipher(symbol, self.rotors[0].ring)
        symbol = self.__encrypt_by_rotors_left(symbol)

        shift = ascii_lowercase.find(symbol) - ascii_lowercase.find(self.rotors[-1].ring)
        symbol = ascii_lowercase[shift]
        symbol = self.__encrypt_plugboard(symbol)

        return symbol.upper()

    def __turn_rotor(self, index: int) -> None:
        if self.rotors[index].turn():
            self.__turn_rotor(index=index - 1)

    def __encrypt_by_rotors_right(
        self,
        symbol: str,
    ) -> str:
        rotors = self.rotors[::-1]
        for i, rotor in enumerate(rotors):
            previus_rotor_ring = self.rotors[len(self.rotors) - i].ring if i >= 1 else None
            symbol = rotor.encipher_right(symbol=symbol, previus_rotor_ring=previus_rotor_ring)
        return symbol

    def __encrypt_by_rotors_left(
        self,
        symbol: str,
    ) -> str:
        for i, rotor in enumerate(self.rotors):
            next_rotor_ring = self.rotors[i - 1].ring if i >= 1 else None
            symbol = rotor.encipher_left(symbol=symbol, next_rotor_ring=next_rotor_ring)
        return symbol

    def __encrypt_plugboard(self, symbol: str) -> str:
        for pair in self.plugboard:
            pair = pair.lower()
            if pair[0] == symbol:
                return pair[1]
            if pair[1] == symbol:
                return pair[0]
        return symbol

    @property
    def rotors_position(self):
        return "".join(x.ring for x in self.rotors)
