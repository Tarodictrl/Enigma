from string import ascii_lowercase
import argparse

from enigma import Enigma
from rotor import rotorb_instance
from reflector import reflectorb_instance
from validator import Validator

logo: str = """
  _____         _                          
 | ____| _ __  (_)  __ _  _ __ ___    __ _ 
 |  _|  | '_ \ | | / _` || '_ ` _ \  / _` |
 | |___ | | | || || (_| || | | | | || (_| |
 |_____||_| |_||_| \__, ||_| |_| |_| \__,_| 
                   |___/                    v1   
                             by: tarodictrl
"""

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-r', '--rotor',
                    help="For example -r ROTOR_II -r ROTOR_I -r ROTOR_III.\nSupport: ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V.\nDefault ROTOR_I, ROTOR_II, ROTOR_III",
                    action='append', choices=rotorb_instance.values, metavar='')
parser.add_argument('-k', '--key', help="For example --key a --key b --key c. Default a, a, a", action='append')
parser.add_argument('--reflector', help="For example UKW_B.\nSupport: UKW_A, UKW_B, UKW_C.\nDefault: UKW_B", choices=reflectorb_instance.values, metavar='', default="UKW_B")
parser.add_argument('--plugboard', help="For example --plugboard AB --plugboard CD", metavar='', default=[], action='append')

args = parser.parse_args()

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
    reflector = reflectorb_instance.build(args.reflector)
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
