from string import ascii_lowercase

from core.enigma import Enigma
from core.rotor import rotorb_instance
from core.reflector import reflectorb_instance
from core.validator import Validator
from core.args import args

logo: str = """
  _____         _                          
 | ____| _ __  (_)  __ _  _ __ ___    __ _ 
 |  _|  | '_ \ | | / _` || '_ ` _ \  / _` |
 | |___ | | | || || (_| || | | | | || (_| |
 |_____||_| |_||_| \__, ||_| |_| |_| \__,_| 
                   |___/                    v1   
                             by: tarodictrl
"""

if __name__ == "__main__":
    print(logo)

    if args.rotor is None:
        args.rotor = ["ROTOR_I", "ROTOR_II", "ROTOR_III"]
    if args.key is None:
        args.key = ["A", "A", "A"]

    reflector = reflectorb_instance.build(args.reflector)
    rotors = [
        rotorb_instance.build(key)
        for key in args.rotor
    ]

    keys = "".join(args.key)
    plugboard = args.plugboard

    Validator.validate_plugboard(plugboard)

    enigma = Enigma(plugboard=plugboard, rotors=rotors, reflector=reflector, keys=keys)
    encrypted = ""

    while True:
        text = input("Write text: ")
        text = "".join(x.lower() for x in text if x.lower() in ascii_lowercase)

        for symbol in text:
            encrypted += enigma.press(symbol)
            if len(encrypted.replace(" ", "")) % 5 == 0:
                encrypted += " "

        print("Encrypted text:", encrypted)
